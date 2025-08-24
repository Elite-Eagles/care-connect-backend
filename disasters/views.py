from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def disaster_list(request):
    disasters = Disaster.objects.all()
    data = DisasterSerializer(disasters, many=True).data
    return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def disaster_create(request):
    serializer = DisasterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)