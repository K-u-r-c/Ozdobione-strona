from django.shortcuts import render
from apps.gallery.models import FAQ

def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})