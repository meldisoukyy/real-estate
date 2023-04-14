from django.urls import path, include
from . import views

urlpatterns = [
    path('contact_form', views.ContactFormView.as_view(), name='contact_form'),
    path('join_form', views.JoinUsFormView.as_view(), name='join_form'),
    path('contract_form', views.ContractRequestFormView.as_view(), name='contract_form'),
    path('add_estate', views.AddEstateView.as_view(), name='add_estate'),
    path('get_estates/', views.GetAllEstatesView.as_view(), name='get_estates'),
    path('get_estate/<int:pk>', views.GetEstateView.as_view(), name='get_estate'),
]
