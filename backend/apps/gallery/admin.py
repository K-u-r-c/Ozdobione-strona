from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Photo, Tag, FAQ
from django.utils.html import mark_safe

@admin.register(Tag)
class TagAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name',)
    ordering = ('order',)

    def has_delete_permission(self, request, obj=None):
        if obj and obj.name in ['Wesele', 'Urodziny', 'Chrzciny']:
            return False
        return super().has_delete_permission(request, obj)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'image_tag')
    search_fields = ('title',)
    filter_horizontal = ('tags',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.clean()

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'image':
            formfield.widget.attrs.update({'onchange': 'previewImage(this);'})
        return formfield

    class Media:
        js = ('js/admin/photo_preview.js',)

@admin.register(FAQ)
class FAQAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('question', 'order')
    search_fields = ('question',)
    ordering = ('order',)