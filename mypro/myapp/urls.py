from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('main',views.main,name="main"),
    path('first',views.first,name="first"),
    path('second',views.second,name="second")
    
]