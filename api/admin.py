from django.contrib import admin
from .models import ContactForm,JoinUsForm, Building
# Register your models here.


admin.site.register(ContactForm)
admin.site.register(JoinUsForm)
admin.site.register(Building)