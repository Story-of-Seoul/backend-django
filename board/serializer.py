from rest_framework import serializers

from account.serializers import ProfileSerializer
from board.models import Board, Comment


class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("pk", "profile", "board", "text")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("board", "text")


class BoardSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Board
        fields = ("pk", "profile", "title", "contents", "request_data_type", "answer",
                  "processing_status", "board_type", "likes", "created_at", 'comments')


class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ("title", "contents", "board_type")



