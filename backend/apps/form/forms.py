from django import forms
from .models import FormField

class DynamicContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DynamicContactForm, self).__init__(*args, **kwargs)
        fields = FormField.objects.all()
        for field in fields:
            if field.field_type == 'char':
                self.fields[field.label] = forms.CharField(label=field.label, required=field.required)
            elif field.field_type == 'email':
                self.fields[field.label] = forms.EmailField(label=field.label, required=field.required)
            elif field.field_type == 'phone':
                self.fields[field.label] = forms.CharField(label=field.label, required=field.required)
            elif field.field_type == 'textarea':
                self.fields[field.label] = forms.CharField(widget=forms.Textarea, label=field.label, required=field.required)
            elif field.field_type == 'checkbox':
                self.fields[field.label] = forms.BooleanField(label=field.label, required=field.required)
            elif field.field_type == 'multiselect':
                choices = [(option.id, option.option_text) for option in field.options.all()]
                self.fields[field.label] = forms.MultipleChoiceField(choices=choices, widget=forms.CheckboxSelectMultiple, label=field.label, required=field.required)