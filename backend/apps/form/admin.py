from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import FormField

@admin.register(FormField)
class FormFieldAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('label', 'field_type', 'required', 'order')
    list_filter = ('field_type', 'required')
    search_fields = ('label',)
    fieldsets = (
        (None, {
            'fields': ('label', 'field_type', 'required', 'order')
        }),
    )
    verbose_name = "Pole formularza"
    verbose_name_plural = "Pola formularza"