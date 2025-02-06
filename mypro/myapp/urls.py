from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),  # Add trailing slash here
    path('', views.index, name='index'),           # This is fine for the homepage (root)
    path('home/', views.home, name='home'),        # Add trailing slash here
]
