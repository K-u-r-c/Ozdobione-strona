from django.contrib import admin
from .models import Photo, Video

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    fields = ('title', 'video_url', 'embed_code', 'created_at')
    readonly_fields = ('created_at',)