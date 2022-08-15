from http import client
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import urllib.request
client_id = 'mrceuxFaYpPo8uVTtmIu'
client_secret = '84efP84YPw'



# Create your views here.
class NewsView(APIView):
    def get(self, request):
        print(request.GET)
        query = request.GET['dataType']
        print('키워드 = ' + query)
        encText = urllib.parse.quote(query)
        
        url = "https://openapi.naver.com/v1/search/news?query=" + encText
        naverRequest = urllib.request.Request(url)
        naverRequest.add_header("X-Naver-Client-Id",client_id)
        naverRequest.add_header("X-Naver-Client-Secret", client_secret)
        
        response = urllib.request.urlopen(naverRequest)
        rescode = response.getcode()
        if(rescode == 200):
            response_body = response.read()
            print('result = ', response_body.decode('utf-8'))
            
            return Response(response_body, status = status.HTTP_200_OK)
            
        else:
            print("Error Code: " + rescode)
        

    
