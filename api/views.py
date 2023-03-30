from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import ContactFormSerializer, JoinUsFormSerializer, BuildingSerializer
from accounts.models import User


# Create your views here.
class ContactFormView(APIView):
    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)


class JoinUsFormView(APIView):
    def post(self, request):
        serializer = JoinUsFormSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)


class AddEstateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id
        serializer = BuildingSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)

