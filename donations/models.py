from django.db import models

# Create your models here.
class Donation(models.Model):
    donor_name = models.CharField(max_length=255)
    donor_email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)