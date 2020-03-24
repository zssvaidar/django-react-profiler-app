from django.urls import path
from .views import ServiceListView, ServiceView
urlpatterns = [
    path('', ServiceListView.as_view(), name='services'),
    path('<int:pk>/', ServiceView.as_view(), name= 'service'),


]
