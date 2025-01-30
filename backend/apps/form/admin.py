from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import FormField, FormFieldOption, FormType

@admin.register(FormType)
class FormTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class FormFieldOptionInline(admin.TabularInline):
    model = FormFieldOption
    extra = 1

@admin.register(FormField)
class FormFieldAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('label', 'field_type', 'required', 'order')
    list_filter = ('field_type', 'required')
    search_fields = ('label',)
    filter_horizontal = ('form_types',)
    fieldsets = (
        (None, {
            'fields': ('label', 'field_type', 'required', 'order', 'form_types')
        }),
    )
    verbose_name = "Pole formularza"
    verbose_name_plural = "Pola formularza"

    def get_inline_instances(self, request, obj=None):
        inlines = []
        if obj and obj.field_type == 'multiselect':
            inlines.append(FormFieldOptionInline(self.model, self.admin_site))
        return inlines

@admin.register(FormFieldOption)
class FormFieldOptionAdmin(admin.ModelAdmin):
    list_display = ('form_field', 'option_text')
    search_fields = ('option_text',)