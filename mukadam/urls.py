from django.urls import path
from mukadam import views
urlpatterns = [
    path('mukadam_dashboard/', views.mukadam_dashboard, name='mukadam_dashboard')
]