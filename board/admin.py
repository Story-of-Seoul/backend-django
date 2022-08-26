from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Board, Comment

# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_filter = ['board_type']
    list_display = ['board_type', 'title', 'author', 'created_at']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ['board']
    list_display = ['text', 'profile', 'board']