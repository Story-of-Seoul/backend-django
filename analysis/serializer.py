from rest_framework import serializers

from analysis.models import DrunkDriving


class DrunkDrivingSerializer(serializers.ModelSerializer):

    class Meta:
        model = DrunkDriving
        fields = ('year', 'county', 'acc_cnt', 'deaths_cnt', 'injuries_cnt')