from rest_framework import serializers
from .models import Post

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "contents", "created_at")
        
class NoticeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "contents")