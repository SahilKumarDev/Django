from django.http import HttpResponse;
from django.shortcuts import render

def home(req):
  # return HttpResponse("Hello, world. You're at the Home page.")
  return render(req, 'website/index.html')

def about(req):
  # return HttpResponse("Hello, world. You're at the polls of About.")
  return render(req, "website/about.html")


def contact(req):
  # return HttpResponse("Hello, world. You're at the polls of Contact.")
  return render(req, "website/contact.html")
