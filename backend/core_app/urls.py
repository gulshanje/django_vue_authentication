from django.urls import path, include
from .views import (
    RegisterAPIView, LoginAPIView, 
    UserAPIView, RefreshTokenAPIView, 
    LogoutAPIView, ResetPasswordAPIView
)
urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('refresh', RefreshTokenAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
     path('reset', ResetPasswordAPIView.as_view()),
]
