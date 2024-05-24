"""
URL configuration for villanorDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include 

# This is a views file import
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Its a config which you have to write when to load a static page on web server
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    # IT IS PASS OF URLS IN APP OR PASS ROUTES IN THEM
    path('villan/', include('villan.urls')),
    
    
    # For the hot reload of web page IT ALWAYS AT THE BOTTOM OF ALL PATH
     path("__reload__/", include("django_browser_reload.urls")),
]
