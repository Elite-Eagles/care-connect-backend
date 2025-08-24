from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import *
from .serializers import *

@api_view(['POST', 'PUT'])
@permission_classes([IsAuthenticated])
def help_request_create(request):
    if request.method == 'POST':
        serializer = HelpRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)
    elif request.method == 'PUT':
        help_request = HelpRequest.objects.get(id=int(request.data.get('id')))
        help_request.status = request.data.get('status', help_request.status)
        help_request.save() 
        return Response({'message': 'Help request updated'}, status=200)
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_help_request(request):
    help_requests = HelpRequest.objects.filter(user=request.user)
    data = HelpRequestSerializer(help_requests, many=True).data
    return Response(data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def all_help_requests(request):
    help_requests = HelpRequest.objects.all()
    data = AdminHelpRequestSerializer(help_requests, many=True).data
    return Response(data)

