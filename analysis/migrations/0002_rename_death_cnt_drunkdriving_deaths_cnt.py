# Generated by Django 3.2.10 on 2022-08-21 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drunkdriving',
            old_name='death_cnt',
            new_name='deaths_cnt',
        ),
    ]