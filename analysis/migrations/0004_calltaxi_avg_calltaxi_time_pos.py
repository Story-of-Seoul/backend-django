# Generated by Django 4.1 on 2022-08-22 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0003_population'),
    ]

    operations = [
        migrations.CreateModel(
            name='calltaxi_avg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('car_num', models.IntegerField()),
                ('receipt_num', models.IntegerField()),
                ('ride_num', models.IntegerField()),
                ('waiting_avg', models.FloatField()),
                ('fare_avg', models.FloatField()),
                ('distance_ride_avg', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='calltaxi_time_pos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('cartype', models.CharField(max_length=20)),
                ('receipttime', models.TextField()),
                ('proccessed_receipttime', models.DateTimeField()),
                ('settime', models.DateTimeField()),
                ('ridetime', models.DateTimeField()),
                ('startpos', models.CharField(max_length=10)),
                ('endpos', models.CharField(max_length=10)),
            ],
        ),
    ]