from django.db import models

# Create your models here.
class Resource(models.Model):
    description = models.TextField()
    location = models.CharField(max_length=10000)
    contact_info = models.CharField(max_length=1000)
    type = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)