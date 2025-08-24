from rest_framework.serializers import ModelSerializer
from .models import *

class VolunteerSerializer(ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }