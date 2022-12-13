
from django.contrib import admin
from django.urls import path
from personal.views import *
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('power/', admin.site.urls),
    path('', ProjectView, name="project"),
    path('project/<int:pk>/', ProjectDetail, name='project'),
    path('blog', BlogIndex, name='blog'),
    path('blog/<str:pk>/', BlogDetail, name='blog_detail'),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
