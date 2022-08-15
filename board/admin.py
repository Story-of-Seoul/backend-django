from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created_at'
        'boardtype'
    )
    search_fields = ('title', 'content', 'author__user_')