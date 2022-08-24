# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountProfile(models.Model):
    user = models.OneToOneField('AuthUser', models.DO_NOTHING, primary_key=True)
    age = models.IntegerField()
    region = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    nickname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'account_profile'


class AnalysisAwareness(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=50)
    very_safe = models.IntegerField()
    relatively_safe = models.IntegerField()
    normal = models.IntegerField()
    relatively_unsafe = models.IntegerField()
    very_unsafe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analysis_awareness'


class AnalysisCalltaxiAvg(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    car_num = models.IntegerField()
    receipt_num = models.IntegerField()
    ride_num = models.IntegerField()
    waiting_avg = models.FloatField()
    fare_avg = models.FloatField()
    distance_ride_avg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analysis_calltaxi_avg'


class AnalysisCalltaxiTimePos(models.Model):
    id = models.BigAutoField(primary_key=True)
    no = models.IntegerField()
    cartype = models.CharField(max_length=20)
    receipttime = models.TextField()
    settime = models.TextField()
    ridetime = models.TextField()
    startpos = models.CharField(max_length=10)
    endpos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'analysis_calltaxi_time_pos'


class AnalysisCaracc(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.IntegerField()
    acc_cl_name = models.CharField(max_length=48)
    place_code = models.CharField(max_length=48)
    acc_cnt = models.IntegerField()
    acc_rate = models.FloatField()
    deaths_cnt = models.IntegerField()
    injuries_cnt = models.IntegerField()
    injuries_rate = models.FloatField()
    speeding_cnt = models.IntegerField(blank=True, null=True)
    center_line_cnt = models.IntegerField(blank=True, null=True)
    sig_violation_cnt = models.IntegerField(blank=True, null=True)
    unsafe_distance_cnt = models.IntegerField(blank=True, null=True)
    unsafe_driving_cnt = models.IntegerField(blank=True, null=True)
    violation_ped_prt_cnt = models.IntegerField(blank=True, null=True)
    deaths_rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'analysis_caracc'


class AnalysisDrunkdriving(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.IntegerField()
    county = models.CharField(max_length=45)
    acc_cnt = models.IntegerField()
    deaths_cnt = models.IntegerField()
    injuries_cnt = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analysis_drunkdriving'


class AnalysisEarthquake(models.Model):
    id = models.BigAutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    distance_from_seoul = models.FloatField()
    scale = models.FloatField()
    epicenter = models.TextField()

    class Meta:
        managed = False
        db_table = 'analysis_earthquake'


class AnalysisEarthquakeResistance(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    total_building = models.IntegerField()
    resistance_required_building = models.IntegerField()
    resistance_equipped_building = models.IntegerField()
    resistance_unequipped_building = models.IntegerField()
    rate_of_total_building = models.FloatField()
    rate_of_required_building = models.FloatField()

    class Meta:
        managed = False
        db_table = 'analysis_earthquake_resistance'


class AnalysisOldmanacc(models.Model):
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

    class Meta:
        managed = False
        db_table = 'analysis_oldmanacc'


class AnalysisPopulation(models.Model):
    id = models.BigAutoField(primary_key=True)
    area = models.CharField(max_length=20)
    total = models.IntegerField()
    korean = models.IntegerField()
    foreign = models.IntegerField()
    senior = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analysis_population'


class AnalysisSeoulDust(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    area = models.CharField(max_length=10, blank=True, null=True)
    nitrogen_dioxide = models.FloatField(blank=True, null=True)
    ozone = models.FloatField(blank=True, null=True)
    carbon_monoxide = models.FloatField(blank=True, null=True)
    sulfur_dioxide = models.FloatField(blank=True, null=True)
    fine_dust = models.IntegerField(blank=True, null=True)
    ultra_fine_dust = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analysis_seoul_dust'


class AnalysisSeoulTemperature(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    area = models.CharField(max_length=10)
    temperature = models.FloatField()
    humidity = models.FloatField()
    rainfall = models.FloatField()

    class Meta:
        managed = False
        db_table = 'analysis_seoul_temperature'


class AnalysisShelter(models.Model):
    id = models.BigAutoField(primary_key=True)
    area = models.CharField(max_length=20)
    shelter_name = models.CharField(max_length=40)
    detail_address = models.TextField()
    acceptance_area = models.IntegerField()
    people_capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'analysis_shelter'


class AnalysisTestTimePos(models.Model):
    id = models.BigAutoField(primary_key=True)
    no = models.IntegerField()
    cartype = models.CharField(max_length=20)
    receipttime = models.TextField()
    settime = models.TextField()
    ridetime = models.TextField()
    startpos = models.CharField(max_length=10)
    endpos = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'analysis_test_time_pos'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class BoardBoard(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=64)
    contents = models.TextField()
    request_data_type = models.CharField(max_length=64)
    answer = models.TextField()
    processing_status = models.CharField(max_length=12)
    board_type = models.CharField(max_length=12)
    created_at = models.DateTimeField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)
    profile = models.ForeignKey(AccountProfile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board_board'


class BoardBoardLikes(models.Model):
    board = models.ForeignKey(BoardBoard, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board_board_likes'
        unique_together = (('board', 'user'),)


class BoardComment(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.TextField()
    author = models.ForeignKey(AuthUser, models.DO_NOTHING)
    board = models.ForeignKey(BoardBoard, models.DO_NOTHING)
    profile = models.ForeignKey(AccountProfile, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'board_comment'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
