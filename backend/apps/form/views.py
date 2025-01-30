from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .forms import DynamicContactForm
from .models import FormField, FormType

def contact_form(request):
    form_types = FormType.objects.all()
    selected_form_type = None

    if request.method == 'POST':
        form_type_id = request.POST.get('form_type')
        if form_type_id:
            selected_form_type = FormType.objects.get(id=form_type_id)
            form = DynamicContactForm(selected_form_type, request.POST)
            if form.is_valid():
                # Process form data
                form_data = form.cleaned_data

                # Convert selected option IDs to names for multiselect fields
                for field in FormField.objects.filter(field_type='multiselect'):
                    if field.label in form_data:
                        selected_ids = form_data[field.label]
                        selected_names = [option.option_text for option in field.options.filter(id__in=selected_ids)]
                        form_data[field.label] = ', '.join(selected_names)

                # Convert boolean values to strings
                for key, value in form_data.items():
                    if isinstance(value, bool):
                        form_data[key] = "Tak" if value else "Nie"

                # Render email content
                subject = "Nowe zgłoszenie formularza kontaktowego"
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = settings.EMAIL_HOST_USER
                text_content = "\n".join([f"{key}: {value}" for key, value in form_data.items()])
                html_content = render_to_string('emails/contact_form_email.html', {'form_data': form_data})

                # Send email
                email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
                email.attach_alternative(html_content, "text/html")
                email.send()

                return redirect('form_success')
        else:
            form = None
    else:
        form = None
        if 'form_type' in request.GET:
            form_type_id = request.GET.get('form_type')
            if form_type_id:
                selected_form_type = FormType.objects.get(id=form_type_id)
                form = DynamicContactForm(selected_form_type)

    return render(request, 'form.html', {'form': form, 'form_types': form_types, 'selected_form_type': selected_form_type})

def form_success(request):
    return render(request, 'form_success.html')