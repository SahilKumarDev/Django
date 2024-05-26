from django.urls import path

# This is a views file import
from . import views

# localhost:3000/villan

urlpatterns = [    
    # Its a config which you have to write when to load a static page on web server
    path('', views.villan, name="villan"),
    path('<int:villan_id>/', views.villandetails, name="villan_details"),
]
