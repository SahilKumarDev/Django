from django.db import models
from django.utils import timezone # THIS IS FOR A TIME TO STORE

# Create your models here.
class VillanVariety(models.Model):
  VILLAN_TYPE_CHOICE = [
    ('Vi', 'Villan'),
    ('li', 'life'),
    ('re', 'relationship')
  ]
  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='villan/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=VILLAN_TYPE_CHOICE)
  description = models.TextField(default="")
  price = models.TextField(default="") 
  
  
  def __str__(self):
    return self.name