from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsStaffUser
from help_requests.models import HelpRequest
from help_requests.serializers import HelpRequestSerializer
from .models import *
from .serializers import *
from resources.models import Resource
from resources.serializers import ResourceSerializer

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def become_volunteer(request):
    user = request.user
    serializer = VolunteerSerializer(data=request.data)
    if serializer.is_valid():
        user.is_staff = True
        user.save()
        serializer.save(user=user)
        return Response({'message': 'You are now a volunteer'}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffUser])
def get_help_requests(request):
    locations = request.user.volunteer_profile.values_list("location", flat=True)
    help_requests = HelpRequest.objects.filter(location__icontains=locations)
    data = HelpRequestSerializer(help_requests, many=True).data
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsStaffUser])
def get_resources(request):
    locations = request.user.volunteer_profile.values_list("location", flat=True)
    resources = Resource.objects.filter(location__icontains=locations)
    data = ResourceSerializer(resources, many=True).data
    return Response(data)