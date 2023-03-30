from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import jwt, datetime
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer


# Create your views here.


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Registered successfully'}, status=status.HTTP_201_CREATED)


# class LoginView(APIView):
#     def post(self, request):
#         national_id = request.data.get('national_id')
#         password = request.data.get('password')
#         user = User.objects.filter(national_id=national_id).first()
#         if user is None:
#             return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
#         if not user.check_password(password):
#             return Response({'error': 'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)
#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }
#         token = jwt.encode(payload, 'secret', algorithm='HS256')
#         response = Response()
#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token,
#             'status': 'success',
#             "username":user.username,
#             "national_id":national_id,
#             "password":password,
#         }
#         user.token = token
#         return response


# # get authenticated user with his cookie
# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')
#         if not token:
#             return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except:
#             return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
