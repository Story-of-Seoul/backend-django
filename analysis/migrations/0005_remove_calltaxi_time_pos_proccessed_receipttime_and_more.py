# Generated by Django 4.1 on 2022-08-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_calltaxi_avg_calltaxi_time_pos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calltaxi_time_pos',
            name='proccessed_receipttime',
        ),
        migrations.AlterField(
            model_name='calltaxi_time_pos',
            name='ridetime',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='calltaxi_time_pos',
            name='settime',
            field=models.TextField(),
        ),
    ]
