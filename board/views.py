from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
import json

# Create your views here.
class BoardListView(APIView):
    
    def get(self, request):
        if request.data['BoardType'] == 'notice':
            postdata = Post.objects.filter(BoardType = 'notice')
            data = json.loads(serialize('json', postdata))
            return JsonResponse({'items':data})
            
#         if request.data['BoardType'] == 'dataRequest':
        
#         if request.data['BoardType'] == 'citizenParticipation':
        
#         if request.data['BoardType'] == 'dataAnalysis':
        
# class BoardWriteView(APIView):
    
    

# class BoardDeleteView(APIView):
    
    
    
# class BoardModifyView(APIView):
    