from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from rembg import remove
from PIL import Image
import numpy as np
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'index.html')

def index1(request):
    return render(request, 'index1.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def projects(request):
    return render(request, 'projects.html')

def project2(request):
    return render(request, 'project2.html')

def project_details(request):
    return render(request, 'project-details.html')

def services(request):
    return render(request, 'services.html')

def service2(request):
    return render(request, 'service2.html')

def service3(request):
    return render(request, 'service3.html')

def recomnend(request):
    return render(request, 'recomnend.html')

def recommend(request):
    return render(request, 'recommend.html')

from django.shortcuts import render
from .forms import ImageUploadForm
from .utils import remove_background
import os
from django.conf import settings

def upload_and_process_image(request):
    form = ImageUploadForm()
    output_image_url = None  # 초기화

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_path = os.path.join(settings.MEDIA_ROOT, image.name)
            output_image_path = os.path.join(settings.MEDIA_ROOT, 'processed', image.name)
            
            # 이미지 파일 저장
            with open(image_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            # 배경 제거 처리
            remove_background(image_path, output_image_path)

            # 결과 이미지 URL
            output_image_url = settings.MEDIA_URL + 'processed/' + image.name

            return render(request, 'projects.html', 
                          {'form': form, 
                           'output_image_url': output_image_url})

    else:
        form = ImageUploadForm()
        return render(request, 'projects.html', {'form': form})



from django.http import JsonResponse
from django.conf import settings
from .combine import load_and_blend_images, save_combined_image
import os
from datetime import datetime

def combine_images_view(request):
    if request.method == 'POST':
        foreground_image = request.FILES['foreground']
        background_image = request.FILES['background']

        # 파일을 임시 저장
        foreground_path = os.path.join(settings.MEDIA_ROOT, 'processed', foreground_image.name)
        background_path = os.path.join(settings.MEDIA_ROOT,  'processed', background_image.name)
        with open(foreground_path, 'wb+') as f:
            for chunk in foreground_image.chunks():
                f.write(chunk)
        with open(background_path, 'wb+') as f:
            for chunk in background_image.chunks():
                f.write(chunk)

        # 이미지 합성
        result_image = load_and_blend_images(foreground_path, background_path)

        # 결과 이미지 저장 및 URL 생성
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        result_image_name = f"result_{timestamp}.png"
        output_path = os.path.join(settings.MEDIA_ROOT, 'processed', result_image_name)
        save_combined_image(result_image, output_path)
        combined_image_url = os.path.join(settings.MEDIA_URL, 'processed', result_image_name)

        # 결과 이미지 URL을 템플릿에 전달
        return render(request, 'project2.html', {'combined_image_url': combined_image_url})

    else:
        return render(request, 'project.html')


