from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_form, name="contact_form"),
    path('success/', views.form_success, name="form_success"),
]
