from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('signin/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]
