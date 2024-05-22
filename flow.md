# Notes/Way of use Django


## Django :- It is reticula fast and very efficacy


## Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of 


## These all server is on run on cmd/powershell 

## Creating Virtual environment file

1. First Method
- python3 -m venv .venv

2. Second method
- uv venv

##

## To start Virtual environment file

# On macOS and Linux.
- source .venv/bin/activate

# On Windows.
- .venv\Scripts\activate

# Deactivate a file 
- deactivate

##

# To install a file by 
- uv pip install {File name}

example :- uv pip install Django


##  To create a Django Project 
- django-admin startproject {file name}

Example :- django-admin startproject villanorDjango


## To up- into the file by 
- cd {file name}

Example :- cd villanorDjango


## To run a Server or start a project
- python manage.py runserver

- To run in a specific port
- python manage.py runserver {port number}

Example :- 
- python manage.py runserver 3000



## file Structure
- Project level 
- app level


## All data come from manage.py
## All file data with was created setting.py 
## All route was handel by urls.py

## To create route in a views.py


## Flow to create a routes 
- views.py has to create a function or render a file
- in urls.py has define the routes and which file is render form views.py

## Pages was create in the new folder name as "templates"


## To inject a static file in "{% %}" the are known as placeholder

## To use css from another folder by a 
- {% load static %} ## This is top of file

- {% static "file_path" %}

- after this you have to give the setting.py
-- import os

-- STATICFILES_DIRS = [os.path.join (BASE_DIR, 'static')]


## 

## {{for a dynamic data }}


## 

# To create a app in Django 
- python .\manage.py startapp {app name}
- python .\manage.py startapp villan