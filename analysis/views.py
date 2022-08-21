from django.db.models import Avg
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from analysis.models import DrunkDriving
from analysis.serializer import DrunkDrivingSerializer


class GetCountyDrunkDrivingView(APIView):

    def get(self, request):
        counties = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구',
                    '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구',
                    '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구',
                    '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구']

        accidentDeathsAvg2010_2021 = {}
        accidentInjuriesAvg2010_2021 = {}
        accidentOccuredAvg2010_2021 = {}


        for county in counties:
            accidentDeathsAvg2010_2021[county] = round(DrunkDriving.objects.filter(county=county).aggregate(Avg('deaths_cnt'))['deaths_cnt__avg'],2)
            accidentInjuriesAvg2010_2021[county] = round(DrunkDriving.objects.filter(county=county).aggregate(Avg('injuries_cnt'))['injuries_cnt__avg'],2)
            accidentOccuredAvg2010_2021[county] = round(DrunkDriving.objects.filter(county=county).aggregate(Avg('acc_cnt'))['acc_cnt__avg'],2)

        return Response({
            "death_avg":accidentDeathsAvg2010_2021,
            "injuries_avg":accidentInjuriesAvg2010_2021,
            "acc_avg": accidentOccuredAvg2010_2021},status=status.HTTP_200_OK)
