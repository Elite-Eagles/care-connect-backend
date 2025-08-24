from django.db import models

# Create your models here.
class Disaster(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=10000)
    relief_status = models.CharField(max_length=100)
    image = models.ImageField(upload_to='disaster_images/', null=True, blank=True)