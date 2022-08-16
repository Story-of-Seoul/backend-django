from django.urls import path
from rest_framework import routers
from .views import NoticeViewSet

urlpatterns = [
    path('', NoticeViewSet.as_view()),
]
