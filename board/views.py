from urllib import response
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.serializers import serialize
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import User
from .models import Post
from .serializers import NoticeSerializer, NoticeCreateSerializer
import json

# Create your views here.
class NoticeViewSet(APIView):
    
    def get(self, request):
        posts = Post.objects.all()
        serializer = NoticeSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NoticeCreateSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    