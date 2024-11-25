from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('mainpage', views.mainpage),
    path('favorites', views.favorites),
    path('impressions', views.impressions),
    path('mylink', views.mylink),
    path('profile', views.profile),
    path('secondarypage', views.secondarypage),
    path('settings', views.settings),
    path('visits', views.visits),
]