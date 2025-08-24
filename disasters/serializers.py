from rest_framework.serializers import ModelSerializer
from .models import *

class DisasterSerializer(ModelSerializer):
    class Meta:
        model = Disaster
        fields = '__all__'