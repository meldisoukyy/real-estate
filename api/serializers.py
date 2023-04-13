from rest_framework import serializers
from .models import ContactForm,JoinUsForm,Building,ContractRequestForm


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = "__all__"
class ContractRequestFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractRequestForm
        fields = "__all__"
class JoinUsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinUsForm
        fields = "__all__"

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = "__all__"
