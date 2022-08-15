# Generated by Django 4.1 on 2022-08-15 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Answer',
            field=models.TextField(blank=True, verbose_name='답변'),
        ),
        migrations.AlterField(
            model_name='post',
            name='ProcessStatus',
            field=models.CharField(blank=True, max_length=10, verbose_name='처리현황'),
        ),
        migrations.AlterField(
            model_name='post',
            name='RequestDataType',
            field=models.CharField(blank=True, max_length=32, verbose_name='요청데이터타입'),
        ),
    ]
