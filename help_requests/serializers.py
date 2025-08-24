from rest_framework.serializers import ModelSerializer
from accounts.serializers import UserSerializer
from .models import *

class BankDetailsSerializer(ModelSerializer):
    class Meta:
        model = BankDetails
        fields = '__all__'

class HelpRequestSerializer(ModelSerializer):
    bank_details = BankDetailsSerializer(required=False, allow_null=True)
    class Meta:
        model = HelpRequest
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }
    def create(self, validated_data):
        bank_data = validated_data.pop("bank_details", None)
        bank = None
        if bank_data:
            bank = BankDetails.objects.create(**bank_data)
        help_request = HelpRequest.objects.create(
            bank_details=bank,
            **validated_data
        )
        return help_request

class AdminHelpRequestSerializer(ModelSerializer):
    bank_details = BankDetailsSerializer()
    user = UserSerializer()
    class Meta:
        model = HelpRequest
        fields = '__all__'