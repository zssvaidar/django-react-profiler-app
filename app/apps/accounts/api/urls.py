from django.urls import path, include
from .views import RegisterAPI, LoginAPI
urlpatterns = [
    path('api-profiler/auth', include('knox.urls') ),
    path('api-profiler/auth/register', RegisterAPI.as_view()),
    path('api-profiler/auth/login', LoginAPI.as_view()),
]
