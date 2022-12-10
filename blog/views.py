from django.shortcuts import render
from .models import Post,  Comment
from .forms import CommentForm
from django.contrib import messages
# Create your views here.

def BlogIndex(request):
    posts = Post.objects.all().order_by('created_on')
    context = {
        "posts": posts,
    }
    return render(request, 'blog_index.html', context)


def BlogDetail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()
            messages.success(request, f'{comment.author}! comment submitted succesfully')
    
    comments = Comment.objects.filter(post=post).order_by('-created_on')
    count = Comment.objects.filter(post=post).count()   
    return render(request, 'blog_details.html', {'post': post, 'count': count, 'comments': comments, 'form': form})