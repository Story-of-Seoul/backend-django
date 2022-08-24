# Generated by Django 4.1 on 2022-08-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0006_seoul_temperature'),
    ]

    operations = [
        migrations.CreateModel(
            name='seoul_dust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('area', models.CharField(max_length=10)),
                ('nitrogen_dioxide', models.FloatField()),
                ('ozone', models.FloatField()),
                ('carbon_monoxide', models.FloatField()),
                ('sulfur_dioxide', models.FloatField()),
                ('fine_dust', models.IntegerField()),
                ('ultra_fine_dust', models.IntegerField()),
            ],
        ),
    ]