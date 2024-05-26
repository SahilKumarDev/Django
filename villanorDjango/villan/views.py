from django.shortcuts import render
from .models import VillanVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def villan(req):
  villans = VillanVariety.objects.all()
  return render(req, 'villan/villan.html', {'villans': villans})

def villandetails(req, villan_id):
  villan = get_object_or_404(VillanVariety, pk=villan_id)
  return render(req, "villandetails.html", {"villan":villan})