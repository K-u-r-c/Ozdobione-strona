from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Photo, Tag, FAQ

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.name in ['Wesele', 'Urodziny', 'Chrzciny']:
            return False
        return super().has_delete_permission(request, obj)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    filter_horizontal = ('tags',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.clean()
        
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    search_fields = ('question',)
    ordering = ('order',)