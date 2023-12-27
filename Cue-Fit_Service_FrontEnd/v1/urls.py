from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from v1.views import *
from . import views
from .views import combine_images_view

app_name = 'v1'

urlpatterns = [
    path('', index, name='index'),
    path('index.html', index, name='index'),
    path('index1.html', index1, name='index1'),
    path('about.html', about, name='about'),
    path('contact.html', contact, name='contact'),
    path('blog.html', blog, name='blog'),
    path('blog-details.html', blog_details, name='blog_details'),
    path('projects.html', projects, name='projects'),
    path('project2.html', project2, name='project2'),
    path('project-details.html', project_details, name='project_details'),
    path('services.html', services, name='services'),
    path('service2.html', service2, name='service2'),
    path('service3.html', service3, name='service3'),
    path('recomnend.html', recomnend, name='recomnend'),
    path('recommend.html', recommend, name='recommend'),
    path('upload-and-process_image', upload_and_process_image, name='upload_and_process_image'),
    path('combine_images_view', views.combine_images_view, name='combine_images_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
