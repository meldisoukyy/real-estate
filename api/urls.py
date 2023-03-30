from django.urls import path, include
from . import views

urlpatterns = [
    path('contact_form', views.ContactFormView.as_view(), name='contact_form'),
    path('join_form', views.JoinUsFormView.as_view(), name='join_form'),
    path('add_estate', views.AddEstateView.as_view(), name='add_estate'),
]
