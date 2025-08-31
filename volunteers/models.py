from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Volunteer(models.Model):
    aadhar_id = models.IntegerField(unique=True)
    location = models.CharField(max_length=10000)
    phone_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='volunteer_profile')