from django.db import models


# Create your models here.
class DrunkDriving(models.Model):
    year = models.IntegerField()
    county = models.CharField(max_length=45)
    acc_cnt = models.IntegerField()
    deaths_cnt = models.IntegerField()
    injuries_cnt = models.IntegerField()


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
