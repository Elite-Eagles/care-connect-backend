from rest_framework.serializers import ModelSerializer
from .models import *

class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'