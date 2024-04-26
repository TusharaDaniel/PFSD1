from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('artistpost/',views.artistpost, name='artistpost'),
    path('add_artist_details',views.add_artist_details,name='add_artist_details'),
    path('view/', views.view_artist_details,name='view_artist_details'),


]