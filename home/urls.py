from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mukadam_logout/', views.mukadam_logout, name='mukadam_logout'),
    path('vehicle_logout/', views.vehicle_logout, name='vehicle_logout'),
]