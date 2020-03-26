from django.urls import path
from .views import ServiceListView, ServiceView
urlpatterns = [
    path('api-profiler/services', ServiceListView.as_view(), name='services'),
    path('api-profiler/services/<int:pk>', ServiceView.as_view(), name= 'service'),
]
