from rest_framework.serializers import ModelSerializer
from .models import *

class DonationSerializer(ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'