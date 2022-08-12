from django.urls import path
from .views import RegisterView, LoginView, SendMailView

urlpatterns = [
    path('signin/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('signin/email', SendMailView.as_view()),
]
