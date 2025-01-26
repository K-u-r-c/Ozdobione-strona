from django.shortcuts import render
from .models import Photo, Video

def photo_gallery(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'photos.html', {'photos': photos})

def video_gallery(request):
    videos = Video.objects.all().order_by('-created_at')
    return render(request, 'videos.html', {'videos': videos})