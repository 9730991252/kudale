from django.urls import path
from owner import views
urlpatterns = [
    path('owner_dashbord/', views.owner_dashbord, name='owner_dashbord'),
    path('add_mukadam/', views.add_mukadam, name='add_mukadam'),
    path('taneg/', views.taneg, name='taneg'),
    path('karkhana/', views.karkhana, name='karkhana'),
    path('vehicle/', views.vehicle, name='vehicle'),
]