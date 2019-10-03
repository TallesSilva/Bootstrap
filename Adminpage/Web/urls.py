from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('configure/', views.configure, name='configure'),
    path('user/', views.user, name='user'),
    path('entrie/', views.entrie, name='entrie'),
    path('about/', views.about, name='about'),
    path('option/', views.option, name='option'),
]