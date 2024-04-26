from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('viewposts', views.viewposts, name='viewposts'),
    path('languages',views.languages,name='telugu'),
    path('bollywood',views.bollywood,name='hindi'),
    path('hollywood',views.hollywood,name='english'),
    path('tamilhits',views.tamilhits,name='tamil'),
    path('hiphop',views.hiphop,name='hiphop')

]
