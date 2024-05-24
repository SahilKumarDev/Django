## NOTES OF DJANGO PROJECT FROM SCRATCH

## NOTES LINK [Link](https://www.notion.so/Django-3a82adcbb9a54dabaa052fc95b08c219?pvs=4)

## 1. Create a virtual environment

## 2. Install Django

## 3. Create a project

## 4. Create an app

## 5. Create a model

## 6. Create a view

## 7. Create a template

## 8. Create a URL

## 9. Create a superuser

## 10. Create a database

## 11. Create a migration

## 12. Run the migration

## 13. Create a static file

## 14. Create a media file

## 15. Create a template tag

## 16. Create a template filter

## 17. Create a custom user model

## 18. Create a custom user manager

## 19. Create a custom user permissions

## 20. Create a custom user groups

## you have to create a templates inside a app or a outside a template folder

```
└── 📁villan  <!-- It is a app level -->
    └── admin.py
    └── apps.py
    └── 📁migrations
        └── __init__.py
    └── models.py
    └── 📁templates  <!-- it is a template where all the file place. -->
        └── 📁villan
            └── all_villan.html
    └── tests.py
    └── views.py
    └── __init__.py
```
###################################


# to run the app which on the server follow the steps

## urls.py

- you have to create a file of urls.py
- flow all the steps what is do in past

```

from django.urls import path

# This is a views file import
from . import views

# localhost:3000/villan

urlpatterns = [
    # Its a config which you have to write when to load a static page on web server
    path('', views.villan, name="villan"),
]


```

- you have to create a url for the app
- you have to use include

```
from django.contrib import admin
from django.urls import path, ## include

# This is a views file import
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),

    # Its a config which you have to write when to load a static page on web server
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),

    path('villan/', include('villan.urls')),
]


```






### Templates in django by jinga

# you can create a layout for all the  file 


 
-- you can create a layout in main templates file which is 

```
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>
    
    {% block title %}   // this is unnamed block THEY VARIOUS TYPE 
    default Value
    {% endblock %}
  </title>

  <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
  
  <nav>This is navabr</nav>


  {% block content %}{% endblock %}


</body>
</html>
```




## this is sa method of writting a  layout

```
{% extends "layout.html" %} 


{% block title %}
  All villan
{% endblock %}

{% block content %}
  <h1>This is home page of villan app</h1>
{% endblock %} 
```


# Tailwind css use

1. python -m pip install django-tailwind
1. uv pip install django-tailwind

2. python -m pip install 'django-tailwind[reload]'
2. uv pip install 'django-tailwind[reload]'

uv pip manage.py tailwind install 
'tailwind[reload]'



pip manage.py tailwind install 






cd  villanordjango =:  python manage.py tailwind init,
python manage.py tailwind install


<!-- Configuration -->

```

INSTALLED_APPS = [
      # Tailwind
    'tailwind',
    'theme',
    
    # For hot reload
     'django_browser_reload'
]

# It is a configure of tailwind in a your app
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = ['127.0.0.1']

# 
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"


MIDDLEWARE = [
    # For hot reload of web page
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]


urlpatterns = [
    
    # For the hot reload of web page IT ALWAYS ATT THE BOTTOM OF ALL PATH
     path("__reload__/", include("django_browser_reload.urls")),
]

```


<!--  yOU HAVE to run in the second terminal to run tailwind by a command  -->
python manage.py tailwind start




in the theme section you have to go to templates 

```
{% load static tailwind_tags %} // IT add in the top of the html file 

<Head> 

		{% tailwind_css %} // IT add in the head section of the html file 
</head>

```

and now it is ready to use in all the section


all the daata form the 

https://django-tailwind.readthedocs.io/en/latest/installation.html



