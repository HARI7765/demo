from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.main,name="main"),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),  # Delete user URL

   
    
]