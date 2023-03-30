from rest_framework import serializers
from .models import ContactForm,JoinUsForm,Building


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"

class JoinUsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinUsForm
        fields = "__all__"

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"
