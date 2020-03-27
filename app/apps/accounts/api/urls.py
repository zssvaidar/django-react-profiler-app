from django.urls import path, include
from .views import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
urlpatterns = [
    path('api-profiler/auth', include('knox.urls') ),
    path('api-profiler/auth/register', RegisterAPI.as_view()),
    path('api-profiler/auth/login', LoginAPI.as_view()),
    path('api-profiler/auth/user', UserAPI.as_view()),
    path('api-profiler/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
]
