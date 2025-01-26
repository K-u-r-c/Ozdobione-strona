from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .forms import DynamicContactForm

def contact_form(request):
    if request.method == 'POST':
        form = DynamicContactForm(request.POST)
        if form.is_valid():
            # Process form data
            form_data = form.cleaned_data
            
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
        form = DynamicContactForm()
    return render(request, 'form.html', {'form': form})

def form_success(request):
    return render(request, 'form_success.html')