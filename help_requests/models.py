from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class HelpRequest(models.Model):
    description = models.TextField()
    aadhar_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=10000)
    status = models.CharField(max_length=100, default='open')
    image = models.ImageField(upload_to='help_request_images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    bank_details = models.ForeignKey('BankDetails', on_delete=models.CASCADE, null=True, blank=True)

class BankDetails(models.Model):
    account_number = models.CharField(max_length=50)
    ifsc_code = models.CharField(max_length=20)