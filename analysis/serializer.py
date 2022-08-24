from rest_framework import serializers
from analysis.models import awareness, earthquake, earthquake_resistance, shelter, population, calltaxi_avg, calltaxi_time_pos, seoul_temperature, seoul_dust

class ShelterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = shelter
        fields = ('area', 'shelter_name', 'detail_address', 'acceptance_area', 'people_capacity')
        
class AwarenessSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = awareness
        fields = ('category', 'very_safe', 'relatively_safe', 'normal', 'relatively_unsafe', 'very_unsafe')
        
class EarthquakeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = earthquake
        fields = ('latitude', 'longitude', 'distance_from_seoul', 'scale', 'epicenter')
        
class EarthquakeResistanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = earthquake_resistance
        fields = ('category', 'type', 'total_building', 'resistance_required_building', 'resistance_equipped_building',
                  'resistance_unequipped_building', 'rate_of_total_building', 'rate_of_required_building')
        
class PopulationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = population
        fields = ('area', 'total', 'korean', 'foreign', 'senior')
        
class CallTaxiAVGSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = calltaxi_avg
        fields = ('date', 'car_num', 'receipt_num', 'ride_num', 'waiting_avg', 'fare_avg', 'distance_ride_avg')

class CallTaxiTimePosSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = calltaxi_time_pos
        fields = ('no', 'cartype', 'receipttime', 'settime', 'ridetime', 'startpos', 'endpos')        
        
class SeoulTemperatureSerializer(serializers.Serializer):
    
    class Meta:
        model = seoul_temperature
        fields = ('date', 'area', 'temperature', 'humidity', 'rainfall')
        
class SeoulDustSerializer(serializers.Serializer):
    
    class Meta:
        model = seoul_dust
        fields = ('date', 'area', 'nitrogen_dioxide', 'ozone', 'carbon_monoxide', 'sulfur_dioxide', 'fine_dust', 'ultra_fine_dust')