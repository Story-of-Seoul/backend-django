import time, datetime, requests, json, csv, pandas
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Max, Sum, Avg, Count

from analysis.serializer import EarthquakeSerializer, EarthquakeResistanceSerializer, ShelterSerializer, AwarenessSerializer, PopulationSerializer, CallTaxiAVGSerializer, CallTaxiTimePosSerializer,SeoulTemperatureSerializer, SeoulDustSerializer
from analysis.models import earthquake, earthquake_resistance, awareness, shelter, population, calltaxi_avg, calltaxi_time_pos, seoul_temperature, seoul_dust, test_time_pos, CarAcc, DrunkDriving, Oldmanacc, calltaxi_iot_data
# Create your views here.


class Test(APIView):
    def get(self, request):
        # for k in range(221,229):
        #     date = k
        #     url = requests.get('http://api.seoulhackathon.kr/inquiry/U2VvdWxIYWNrYXRob24yMDIy/20/1?inqDt=20210'+str(date))
        #     data = json.loads(url.text)
        #     tmplist = []
        #     for i in range(0, len(data['result_data'])):
        #         tmp = {'car_num': data['result_data'][i]['column2'], 'on_time':data['result_data'][i]['column5'],
        #                 'off_time':data['result_data'][i]['column7'], 'safe_rate':data['result_data'][i]['column9'], 'acceleration' : data['result_data'][i]['column10'],
        #                 'deceleration':data['result_data'][i]['column11'], 'speeding':data['result_data'][i]['column12'], 'ride_time':data['result_data'][i] ['column14']}
        #         tmplist.append(tmp)
        #     df = pandas.json_normalize(tmplist)
        #     df.to_csv("csv\iot_calltaxi0"+str(date)+'.csv', index=False, encoding="utf-8-sig")
        
        return Response(status=status.HTTP_200_OK)
        
class GetSafe(APIView):
    
    def get(self, request):
        safe = {}
        
        EarthquakeFrequency = earthquake.objects.count()
        safe['earthquake'] = EarthquakeFrequency
        
        
        AwarenessQueryset = awareness.objects.values()
        AwarenessData = {}
        
        for query in AwarenessQueryset:
            AwarenessData[query["category"]] = query["relatively_unsafe"]+query["very_unsafe"]
        safe['awareness'] = AwarenessData


        ResistanceQueryset = earthquake_resistance.objects.values()
        ResistanceData = {}
        
        for query in ResistanceQueryset:
            list_a = []
            list_a.append(query["total_building"])
            list_a.append(query["resistance_unequipped_building"])
            ResistanceData[query["category"]] = list_a
        safe['building'] = ResistanceData
        
        
        countries = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구',
                    '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구',
                    '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구',
                    '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
        country_population = {}
        people_capacity = {}
        capacity_rate = {}
        
        for country in countries:
            country_population[country] = population.objects.filter(area=country).aggregate(Sum('total'))['total__sum']
            people_capacity[country] = shelter.objects.filter(area=country).aggregate(Sum('people_capacity'))['people_capacity__sum']
            capacity_rate[country] = round(
                float(country_population[country])/float(people_capacity[country])*100,2
            )
        safe['shelter'] = {"population":country_population,
                         "capacity":people_capacity,
                         "rate":capacity_rate}
        
        return Response(safe, status=status.HTTP_200_OK)
        

class GetDisableCallTaxi(APIView):
    
    def get(self, request):
        DisableCallTaxi = {}
        
        CallFrequency = calltaxi_time_pos.objects.count()
        DisableCallTaxi['calltotal'] = CallFrequency
        
        
        WaitingTime = calltaxi_avg.objects.aggregate(Avg('waiting_avg'))
        DisableCallTaxi['waiting'] = round(WaitingTime["waiting_avg__avg"])
        
        
        day = {"01":0, "02":0, "03":0, "04":0, "05":0, "06":0, "07":0, "08":0, "09":0, 
               "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0,
               "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0, "30":0, "31":0, }
        week = {"Mon":0, "Tue":0, "Wed":0, "Thu":0, "Fri":0, "Sat":0, "Sun":0}
        time = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, 
                "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0}

        dataset = calltaxi_time_pos.objects.values('receipttime')
        
        for data in dataset:
            test = data["receipttime"]
        
            # test = '2022-07-24 오전 12:17:00'
            day[test[8:10]] = day[test[8:10]] + 1
            
            if int(test[8:10]) in (4, 11, 18, 25):
                week["Mon"] = week["Mon"] + 1
            elif int(test[8:10]) in (5, 12, 19, 26):
                week["Tue"] = week["Tue"] + 1
            elif int(test[8:10]) in (6, 13, 20, 27):
                week["Wed"] = week["Wed"] + 1
            elif int(test[8:10]) in (7, 14, 21, 28):
                week["Thu"] = week["Thu"] + 1
            elif int(test[8:10]) in (1, 8, 15, 22, 29):
                week["Fri"] = week["Fri"] + 1    
            elif int(test[8:10]) in (2, 9, 16, 23, 30):
                week["Sat"] = week["Sat"] + 1      
            elif int(test[8:10]) in (3, 10, 17, 24, 31):
                week["Sun"] = week["Sun"] + 1  
            
            tmp1 = test[11:13]
            tmp2 = int(test[-8:-6])
            
            if tmp1 == "오후":
                if tmp2 != 12:
                    tmp2 = tmp2 + 12
            elif tmp1 == "오전" and tmp2 == 12:
                tmp2 = tmp2 - 12

            time[str(tmp2)] = time[str(tmp2)] + 1
        DisableCallTaxi['callfrequency'] = {'day':day.values(),'week':week.values(),'time':time.values()}
        
        
        
        countries = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구',
                    '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구',
                    '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구',
                    '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
        start = {}
        end = {}

        for country in countries:
            countrytmp = country+'\r'
            start[country] = test_time_pos.objects.filter(startpos = country).count()
            end[country] = test_time_pos.objects.filter(endpos = countrytmp).count()
        DisableCallTaxi['callstartend'] = {'startpos':start, 'endpos':end}
        
        
        receipt_set = {"0~5":0, "6~10":0, "11~15":0, "16~20":0, "21~25":0, "26~30":0, "31~35":0, "36~40":0, "이상":0}
        set_ride = {"0~5":0, "6~10":0, "11~15":0, "16~20":0, "21~25":0, "26~30":0, "31~35":0, "36~40":0, "이상":0}
        receipt_ride = {"0~5":0, "6~10":0, "11~15":0, "16~20":0, "21~25":0, "26~30":0, "31~35":0, "36~40":0, "이상":0}
        
        dataset = calltaxi_time_pos.objects.values('receipttime', 'settime', 'ridetime')
        datalen = len(dataset)
        
        for i in range(datalen):
            receipt_set_tmp = datetime.datetime.strptime(dataset[i]['settime'][14:], "%H:%M:%S") - datetime.datetime.strptime(dataset[i]['receipttime'][14:], "%H:%M:%S")
            if 0 <= round(receipt_set_tmp.seconds/60)%720 < 6:
                receipt_set['0~5'] += 1
            elif 5 < round(receipt_set_tmp.seconds/60)%720 < 11:
                receipt_set['6~10'] += 1
            elif 10 < round(receipt_set_tmp.seconds/60)%720 < 16:
                receipt_set['11~15'] += 1
            elif 15 < round(receipt_set_tmp.seconds/60)%720 < 21:
                receipt_set['16~20'] += 1
            elif 20 < round(receipt_set_tmp.seconds/60)%720 < 26:
                receipt_set['21~25'] += 1
            elif 25 < round(receipt_set_tmp.seconds/60)%720 < 31:
                receipt_set['26~30'] += 1
            elif 30 < round(receipt_set_tmp.seconds/60)%720 < 36:
                receipt_set['31~35'] += 1
            elif 35 < round(receipt_set_tmp.seconds/60)%720 < 41:
                receipt_set['36~40'] += 1
            else:
                receipt_set['이상'] += 1
                
            set_ride_tmp = datetime.datetime.strptime(dataset[i]['ridetime'][14:], "%H:%M:%S") - datetime.datetime.strptime(dataset[i]['settime'][14:], "%H:%M:%S")
            if 0 <= round(set_ride_tmp.seconds/60)%720 < 6:
                set_ride['0~5'] += 1
            elif 5 < round(set_ride_tmp.seconds/60)%720 < 11:
                set_ride['6~10'] += 1
            elif 10 < round(set_ride_tmp.seconds/60)%720 < 16:
                set_ride['11~15'] += 1
            elif 15 < round(set_ride_tmp.seconds/60)%720 < 21:
                set_ride['16~20'] += 1
            elif 20 < round(set_ride_tmp.seconds/60)%720 < 26:
                set_ride['21~25'] += 1
            elif 25 < round(set_ride_tmp.seconds/60)%720 < 31:
                set_ride['26~30'] += 1
            elif 30 < round(set_ride_tmp.seconds/60)%720 < 36:
                set_ride['31~35'] += 1
            elif 35 < round(set_ride_tmp.seconds/60)%720 < 41:
                set_ride['36~40'] += 1
            else:
                set_ride['이상'] += 1
                
            receipt_ride_tmp = datetime.datetime.strptime(dataset[i]['ridetime'][14:], "%H:%M:%S") - datetime.datetime.strptime(dataset[i]['receipttime'][14:], "%H:%M:%S")
            if 0 <= round(receipt_ride_tmp.seconds/60)%720 < 6:
                receipt_ride['0~5'] += 1
            elif 5 < round(receipt_ride_tmp.seconds/60)%720 < 11:
                receipt_ride['6~10'] += 1
            elif 10 < round(receipt_ride_tmp.seconds/60)%720 < 16:
                receipt_ride['11~15'] += 1
            elif 15 < round(receipt_ride_tmp.seconds/60)%720 < 21:
                receipt_ride['16~20'] += 1
            elif 20 < round(receipt_ride_tmp.seconds/60)%720 < 26:
                receipt_ride['21~25'] += 1
            elif 25 < round(receipt_ride_tmp.seconds/60)%720 < 31:
                receipt_ride['26~30'] += 1
            elif 30 < round(receipt_ride_tmp.seconds/60)%720 < 36:
                receipt_ride['31~35'] += 1
            elif 35 < round(receipt_ride_tmp.seconds/60)%720 < 41:
                receipt_ride['36~40'] += 1
            else:
                receipt_ride['이상'] += 1
            
        print(receipt_set, set_ride, receipt_ride)           
        DisableCallTaxi['calltime'] = {'receipt_set':receipt_set.values(), 'set_ride':set_ride.values(), 'receipt_ride':receipt_ride.values()}

        calltaxi_iot = {}
        acceleration = []
        deceleration = []
        safe_rate = []
        for m in range(1,13):
            tmp = calltaxi_iot_data.objects.filter(on_time__month = m).aggregate(Sum('acceleration'))['acceleration__sum']
            acceleration.append(tmp)
            tmp = calltaxi_iot_data.objects.filter(on_time__month = m).aggregate(Sum('deceleration'))['deceleration__sum']
            deceleration.append(tmp)
            tmp = round(calltaxi_iot_data.objects.filter(on_time__month = m, safe_rate__gt = 0).aggregate(Avg('safe_rate'))['safe_rate__avg'],2)
            safe_rate.append(tmp)
        calltaxi_iot['acceleration'] = acceleration
        calltaxi_iot['deceleration'] = deceleration
        calltaxi_iot['safe_rate'] = safe_rate
        DisableCallTaxi['calltaxi_iot'] = calltaxi_iot
            
            
        
        # return Response(status=status.HTTP_200_OK)
        return Response(DisableCallTaxi, status=status.HTTP_200_OK)
        
        
class GetEnvironment(APIView):
    
    def get(self, request):
        Environment = {}
        
        countries = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구',
                    '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구',
                    '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구',
                    '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
        
        Dust = {}
        FineDust_09_21 = {}
        UltraFineDust_14_21 = {}
        FineDust = {}
        UltraFineDust = {}
        Temperature = {}
        
        m_field = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 11, 12]
        Temperature_y_field = [2009, 2013, 2017, 2021]
        Dust_y_field = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
        
        for y in Temperature_y_field:
            TmpDataSet = seoul_temperature.objects.filter(date__year = y)
            TmpList = []
            for m in m_field:
                tmp = TmpDataSet.filter(date__month = m).aggregate(Avg('temperature'))['temperature__avg']
                TmpList.append(round(tmp,2))
            Temperature[y] = TmpList
            
        TmpList1 = []
        TmpList2 = []
        for y in Dust_y_field:
            DataSet = seoul_dust.objects.filter(date__year = y)
            tmp = DataSet.aggregate(Avg('fine_dust'))['fine_dust__avg']
            TmpList1.append(tmp)
            tmp = DataSet.aggregate(Avg('ultra_fine_dust'))['ultra_fine_dust__avg']
            TmpList2.append(tmp)
        FineDust['Year'] = TmpList1
        UltraFineDust['Year'] = TmpList2
        
        TmpList1 = []
        TmpList2 = []
        for m in m_field:
            DataSet = seoul_dust.objects.filter(date__month = m)
            tmp = DataSet.aggregate(Avg('fine_dust'))['fine_dust__avg']
            TmpList1.append(tmp)
            tmp = DataSet.aggregate(Avg('ultra_fine_dust'))['ultra_fine_dust__avg']
            TmpList2.append(tmp)
        FineDust['Month'] = TmpList1
        UltraFineDust['Month'] = TmpList2
        
        for country in countries:
            TmpList = []
            tmp = seoul_dust.objects.filter(date__year = 2009, area = country).aggregate(Avg('fine_dust'))['fine_dust__avg']
            TmpList.append(tmp)
            tmp = seoul_dust.objects.filter(date__year = 2021, area = country).aggregate(Avg('fine_dust'))['fine_dust__avg']
            TmpList.append(tmp)
            FineDust_09_21[country] = TmpList
            
            TmpList = []
            tmp = seoul_dust.objects.filter(date__year = 2014, area = country).aggregate(Avg('ultra_fine_dust'))['ultra_fine_dust__avg']
            TmpList.append(tmp)
            tmp = seoul_dust.objects.filter(date__year = 2021, area = country).aggregate(Avg('ultra_fine_dust'))['ultra_fine_dust__avg']
            TmpList.append(tmp)
            UltraFineDust_14_21[country] = TmpList
            
        Dust = {'2009/2021미세먼지' : FineDust_09_21, '2014/2021초미세먼지' : UltraFineDust_14_21, '미세먼지':FineDust, '초미세먼지':UltraFineDust}
        return Response({'Dust':Dust, 'Temperature':Temperature}, status=status.HTTP_200_OK)
            
 
class GetAccident(APIView):
    
    def get(self, request):
        
        year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
        AccidentCategory = ["전체", "스쿨존내어린이사고", "어린이보행사고", "고령운전사고", "고령보행사고"]
        AccidentCategory2 = ["스쿨존내어린이사고", "어린이보행사고", "고령운전사고", "고령보행사고"]
        AccidentCategory3 = ["과속", "중앙선침범", "신호위반", "안전거리미확보", "난폭운전", "보행자보호의무위반"]
        AccidentCategory4 = ["사건발생수", "사망자수", "부상자수"]
        countries = ['종로구', '중구', '용산구', '성동구', '광진구', '동대문구',
                    '중랑구', '성북구', '강북구', '도봉구', '노원구', '은평구',
                    '서대문구', '마포구', '양천구', '강서구', '구로구', '금천구',
                    '영등포구', '동작구', '관악구', '서초구', '강남구', '송파구', '강동구']
        occurrence = {}
        occurrenceEdit = {}
        ChangeRate = {}
        ChangeRateEdit = {}
        cause = {}
        causeEdit = {}
        AccidentMap = {}
        AccidentMapEdit = {}
        DeadRate = {}
        DeadRateEdit = {}
        
        ChangeRate[2010] = {"스쿨존내어린이사고":0, "어린이보행사고":0, "고령운전사고":0, "고령보행사고":0}
        for y in year:
            occurrence_tmp = {} #occurence
            # occurrence_tmp['교통사고'] = CarAcc.objects.filter(year = y, acc_cl_name = '전체').aggregate(Sum('acc_cnt'))['acc_cnt__sum']
            for category in AccidentCategory:
                occurrence_tmp[category] = CarAcc.objects.filter(year = y, acc_cl_name = category).aggregate(Sum('acc_cnt'))['acc_cnt__sum']
            occurrence[y] = occurrence_tmp
            
            ChangeRate_tmp = {}
            if y == 2010:
                continue
            for category in AccidentCategory: #changerate
                ChangeRate_tmp[category] = round(occurrence[y][category]/occurrence[y-1][category],2)
            ChangeRate[y] = ChangeRate_tmp 
        
        for y in year: #cause
            cause_tmp = {}
            drunk_tmp = {}
            data = CarAcc.objects.filter(year=y, place_code='서울시', acc_cl_name='전체').values()
            cause_tmp['과속'] = round(data[0]['speeding_cnt'] / data[0]['acc_cnt'],3)
            cause_tmp['중앙선침범'] = round(data[0]['center_line_cnt'] / data[0]['acc_cnt'],3)
            cause_tmp['신호위반'] = round(data[0]['sig_violation_cnt'] / data[0]['acc_cnt'],3)
            cause_tmp['안전거리미확보'] = round(data[0]['unsafe_distance_cnt'] / data[0]['acc_cnt'],3)
            cause_tmp['난폭운전'] = round(data[0]['unsafe_driving_cnt'] / data[0]['acc_cnt'],3)
            cause_tmp['보행자보호의무위반'] = round(data[0]['violation_ped_prt_cnt'] / data[0]['acc_cnt'],3)
            cause[y] = cause_tmp
            
            
            data2 = DrunkDriving.objects.filter(year=y, county='소계').values() #drunk
            drunk_tmp['사건발생수'] = round(data2[0]['acc_cnt'] / data[0]['acc_cnt'],3)
            drunk_tmp['사망자수'] = round(data2[0]['deaths_cnt'] / data[0]['deaths_cnt'],3)
            drunk_tmp['부상자수'] = round(data2[0]['injuries_cnt'] / data[0]['injuries_cnt'],3)
            DeadRate[y] = drunk_tmp
            
        for country in countries:
            AccidentMap_tmp = {}
            AccidentMap_tmp['사건발생수'] = Oldmanacc.objects.filter(city_and_county_name = country).aggregate(Sum('occurrence_cnt'))['occurrence_cnt__sum']
            AccidentMap_tmp['사망자수'] = Oldmanacc.objects.filter(city_and_county_name = country).aggregate(Sum('deaths_cnt'))['deaths_cnt__sum']
            AccidentMap_tmp['중상자수'] = Oldmanacc.objects.filter(city_and_county_name = country).aggregate(Sum('serious_injuries_cnt'))['serious_injuries_cnt__sum']
            AccidentMap_tmp['경상자수'] = Oldmanacc.objects.filter(city_and_county_name = country).aggregate(Sum('slight_injuries_cnt'))['slight_injuries_cnt__sum']
            AccidentMap[country] = AccidentMap_tmp
        
        
        
        for category in AccidentCategory:
            tmp = {}
            for y in year:
                tmp[y] = occurrence[y][category]
            occurrenceEdit[category] = tmp.values()
            
        for category in AccidentCategory2:
            tmp = {}
            for y in year:
                tmp[y] = ChangeRate[y][category]
            ChangeRateEdit[category] = tmp.values()
            
        for category in AccidentCategory3:
            tmp = {}
            for y in year:
                tmp[y] = cause[y][category]
            causeEdit[category] = tmp.values()
            
        for category in AccidentCategory4:
            tmp = {}
            for y in year:
                tmp[y] = DeadRate[y][category]
            DeadRateEdit[category] = tmp.values()
        
        
        
        return Response({'occurrence':occurrenceEdit,
                            'ChangeRate':ChangeRateEdit,
                            'cause':causeEdit,
                            'AccidentPlace':AccidentMap,
                            'DrunkRate':DeadRateEdit}, status=status.HTTP_200_OK)