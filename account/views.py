from urllib import response
from django.shortcuts import render
from django.core.mail import EmailMessage
from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer, LoginSerializer
import random

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    
class SendMailView(APIView):
    def post(self, request):
        number = random.randrange(10000000, 99999999)
        email = request.data['email']
        if email is not None:
            subject = 'Story of Seoul Verification E-mail'
            message = str(number)
            mail = EmailMessage(subject, message, to=[email])
            mail.send()
            return Response({"정상적으로 발신하였음"}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
class ConfirmMailView(APIView):
    def post(self, request):
        RequestNumber = request.data['number']
        #if RequestNumber == int(origin_number)
        if RequestNumber == '11111111':
            return Response({"정상적으로 인증되었음"}, status=status.HTTP_200_OK)
        else:
            return Response({"인증에 실패하였음"}, status=status.HTTP_400_BAD_REQUEST)