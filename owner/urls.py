from django.urls import path
from owner import views
urlpatterns = [
    path('owner_dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('add_mukadam/', views.add_mukadam, name='add_mukadam'),
    path('taneg/', views.taneg, name='taneg'),
    path('report/', views.report, name='report'),
    path('karkhana/', views.karkhana, name='karkhana'),
    path('vehicle/', views.vehicle, name='vehicle'),
]  