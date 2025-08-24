from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from help_requests.models import HelpRequest
from accounts.permissions import IsStaffUser
from .models import *
from .serializers import *

@api_view(['POST'])
@permission_classes([IsStaffUser])
def resource_create(request):
    serializer = ResourceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_nearby_resources(request):
    location = HelpRequest.objects.filter(user = request.user)[0].location
    resources = Resource.objects.filter(location__icontains=location)
    data = ResourceSerializer(resources,many = True).data
    return Response(data)