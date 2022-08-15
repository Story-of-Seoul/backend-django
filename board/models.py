from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64, verbose_name='글 제목')
    contents = models.TextField(verbose_name='글 내용')
    author = models.ForeignKey('account.User', related_name='posts', on_delete=models.CASCADE, verbose_name='작성자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='글 작성일')
    boardtype = models.CharField(max_length=32, verbose_name='게시판 종류')
    
    RequestDataType = models.CharField(max_length=32, verbose_name='요청데이터타입', blank=True)
    Answer = models.TextField(verbose_name='답변', blank=True)
    ProcessingStatus = models.CharField(max_length=10, verbose_name='처리현황', blank=True)
    
    def __str__(self):
        return self.Title
    
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')