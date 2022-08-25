from rest_framework import serializers
from .models import NewsPolicy

class NewsPolicySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsPolicy
        fields = ['title', 'url', 'content']
        
    # title = serializers.TextField()
    # url = serializers.TextField()
    # content = serializers.TextField()