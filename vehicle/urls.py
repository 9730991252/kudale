from django.urls import path
from vehicle import views
urlpatterns = [
    path('vehicle_dashboard/', views.vehicle_dashboard, name='vehicle_dashboard')
]