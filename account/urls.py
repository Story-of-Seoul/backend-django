from django.urls import path
from .views import SignUpView, EmailSendView, SignInView, MyPageView

urlpatterns = [

    path('signup/', SignUpView.as_view()),
    path('signup/email', EmailSendView.as_view()),
    path('signin/', SignInView.as_view()),
    path('mypage/', MyPageView.as_view()),
]
