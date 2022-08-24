from django.db import models

# Create your models here.
class DrunkDriving(models.Model):
    year = models.IntegerField()
    county = models.CharField(max_length=45)
    acc_cnt = models.IntegerField()
    deaths_cnt = models.IntegerField()
    injuries_cnt = models.IntegerField()
    
    # class Meta:
    #     managed = True
    #     db_table = 'analysis_drunkdriving'

class Oldmanacc(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.IntegerField()
    place_id = models.IntegerField()
    city_and_county_name = models.CharField(max_length=48)
    acc_point = models.CharField(max_length=128)
    occurrence_cnt = models.IntegerField()
    deaths_cnt = models.IntegerField()
    serious_injuries_cnt = models.IntegerField()
    slight_injuries_cnt = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    
class CarAcc(models.Model):
    year = models.IntegerField()
    acc_cl_name = models.CharField(max_length=48)
    place_code = models.CharField(max_length=48)
    acc_cnt = models.IntegerField()
    acc_rate = models.FloatField()
    deaths_cnt = models.IntegerField()
    injuries_cnt = models.IntegerField()
    injuries_rate = models.FloatField()
    speeding_cnt = models.IntegerField(blank=True)
    center_line_cnt = models.IntegerField(blank=True)
    sig_violation_cnt = models.IntegerField(blank=True)
    unsafe_distance_cnt = models.IntegerField(blank=True)
    unsafe_driving_cnt = models.IntegerField(blank=True)
    violation_ped_prt_cnt = models.IntegerField(blank=True)
    
    # class Meta:
    #     managed = True
    #     db_table = 'analysis_caracc'

class awareness(models.Model):
    category = models.CharField(max_length=50)
    very_safe = models.IntegerField()
    relatively_safe = models.IntegerField()
    normal = models.IntegerField()
    relatively_unsafe = models.IntegerField()
    very_unsafe = models.IntegerField()
    
class earthquake_resistance(models.Model):
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    total_building = models.IntegerField()
    resistance_required_building = models.IntegerField()
    resistance_equipped_building = models.IntegerField()
    resistance_unequipped_building = models.IntegerField()
    rate_of_total_building = models.FloatField()
    rate_of_required_building = models.FloatField()
    
class shelter(models.Model):
    area = models.CharField(max_length=20)
    shelter_name = models.CharField(max_length=40)
    detail_address = models.TextField()
    acceptance_area = models.IntegerField()
    people_capacity = models.IntegerField()
    # latitude = models.FloatField(default = '')
    # longitude = models.FloatField(default = )
    # 주소로 위도 경도 구할 수 있을듯 필요하면 합시다
    
class earthquake(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    distance_from_seoul = models.FloatField()
    scale = models.FloatField()
    epicenter = models.TextField()
    
class population(models.Model):
    area = models.CharField(max_length=20)
    total = models.IntegerField()
    korean = models.IntegerField()
    foreign = models.IntegerField()
    senior = models.IntegerField()
    
class calltaxi_avg(models.Model):
    date = models.DateField()
    car_num = models.IntegerField()
    receipt_num = models.IntegerField()
    ride_num = models.IntegerField()
    waiting_avg = models.FloatField()
    fare_avg = models.FloatField()
    distance_ride_avg = models.IntegerField()
    
class calltaxi_time_pos(models.Model):
    no = models.IntegerField()
    cartype = models.CharField(max_length=20)
    receipttime = models.TextField()
    settime = models.TextField()
    ridetime = models.TextField()
    startpos = models.CharField(max_length=10)
    endpos = models.CharField(max_length=10)

class seoul_temperature(models.Model):
    date = models.DateField()
    area = models.CharField(max_length=10)
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()
    
class seoul_dust(models.Model):
    date = models.DateField()
    area = models.CharField(max_length=10)
    nitrogen_dioxide = models.FloatField()
    ozone = models.FloatField()
    carbon_monoxide = models.FloatField()
    sulfur_dioxide = models.FloatField()
    fine_dust = models.IntegerField()
    ultra_fine_dust = models.IntegerField()
    
class test_time_pos(models.Model):
    no = models.IntegerField()
    cartype = models.CharField(max_length=20)
    receipttime = models.TextField()
    settime = models.TextField()
    ridetime = models.TextField()
    startpos = models.CharField(max_length=10)
    endpos = models.CharField(max_length=10)