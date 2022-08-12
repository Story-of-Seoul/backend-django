from urllib import response
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
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
        AuthNumber = random.randrange(10000000, 99999999)
        MailAddress = request.data['email']
        if MailAddress is not None:
            subject = 'Story of Seoul Verification E-mail'
            message = str(AuthNumber)
            mail = EmailMessage(subject, message, to=[MailAddress])
            mail.send()
            return Response({"Authentication Key":AuthNumber}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
  
  
  
        