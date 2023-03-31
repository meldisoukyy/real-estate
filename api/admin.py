from django.contrib import admin
from .models import ContactForm,JoinUsForm, Building
# Register your models here.




class ContactFormAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactForm
        fields = "__all__"



admin.site.register(ContactForm)
admin.site.register(JoinUsForm)
admin.site.register(Building)