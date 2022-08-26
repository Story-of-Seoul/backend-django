import logging
from django.core.mail import EmailMessage
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Profile
from .serializers import SignUpSerializer, SignInSerializer
import random


# Create your views here.
class SignUpView(APIView):

    def post(self, request):

        data = request.data
        userSerializer = SignUpSerializer(data=data)

        if userSerializer.is_valid():
            user = userSerializer.save()
            profile = Profile()
            profile.user = user
            profile.nickname = data['nickname']
            profile.age = data['age']
            profile.region = data['region']
            profile.gender = data['gender']
            profile.save()

            response = userSerializer.data
            response.update({'nickname': data['nickname'],'age': data['age'], "region": data['region'], "gender": data['gender']})

            return Response(response, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class EmailSendView(APIView):
    def post(self, request):
        authNumber = random.randrange(10000000, 99999999)
        receiverEmail = request.data['email']
        if receiverEmail is not None:
            subject = 'Story of Seoul Verification E-mail'
            message = str(authNumber)
            mail = EmailMessage(subject, message, to=[receiverEmail])

            try:
                mail.send()
                print("Email 전송 성공")
                return Response({"authNumber": authNumber},status=status.HTTP_200_OK)
            except:
                print("Email 전송 실패")
                return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class SignInView(generics.GenericAPIView):
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    

class MyPageView(APIView):
    
    def get(self, request):
        profile = Profile.objects.get(user=self.request.user)
        email = request.user.email
        id = profile.user_id
        nickname = profile.nickname
        gender = profile.gender
        region = profile.region
        
        
        return Response({'id': id, 'email':email, 'nickname':nickname, 'gender':gender, 'region':region}, status=status.HTTP_200_OK)
