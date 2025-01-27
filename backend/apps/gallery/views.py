from django.shortcuts import render
from .models import Photo, Tag

def photo_gallery(request):
    default_tags = ['Wesele', 'Urodziny', 'Chrzciny']
    for tag_name in default_tags:
        Tag.objects.get_or_create(name=tag_name)

    selected_tags = request.GET.getlist('tags')
    if selected_tags:
        photos = Photo.objects.filter(tags__name__in=selected_tags).distinct().order_by('-created_at')
    else:
        photos = Photo.objects.all().order_by('-created_at')
    tags = Tag.objects.all()
    return render(request, 'photos.html', {'photos': photos, 'tags': tags, 'selected_tags': selected_tags})