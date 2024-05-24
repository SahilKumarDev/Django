from django.shortcuts import render

# Create your views here.
def villan(req):
  return render(req, 'villan/villan.html')

def allvillan(req):
  return render(req, "allvillan.html")