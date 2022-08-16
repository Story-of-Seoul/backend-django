from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created_at',
        'board_type',
    )
    search_fields = ('title', 'content', 'author__user_username', 'board_type',)
    
admin.site.register(Post, PostAdmin)