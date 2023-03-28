from django.urls import path, include
from . import views

urlpatterns = [
path('contact_form/', views.ContactFormView.as_view(), name='contact_form'),
]