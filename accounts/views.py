from firebase_admin import auth as firebase_auth
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
import random

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    username = User.objects.filter(email=email).first().username if User.objects.filter(email=email).first() else None
    user = authenticate(request, username=username, password=password)
    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['POST'])
def firebase_login_view(request):
    id_token = request.data.get('id_token')
    try:
        decoded_token = firebase_auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        name = decoded_token['name']
        email = decoded_token['email']
        user = User.objects.filter(email = email).first()
        if not user:
            username = name[:3] + uid[:3] + str(random.randint(100, 999))
            user = User.objects.create_user(username=username, email=decoded_token.get('email', ''))
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup_view(request):
    first_name = request.data.get('first_name')
    last_name = request.data.get('last_name')
    email = request.data.get('email')
    password = request.data.get('password')
    if (User.objects.filter(email=email).first()):
        return Response({"error": "user already exists"}, status=status.HTTP_400_BAD_REQUEST)
    username = first_name[:3]+last_name[:2]+str(random.randint(100,999))
    user = User.objects.create_user(username,email,password)
    user.first_name = first_name
    user.last_name = last_name
    user.save()
    refresh = RefreshToken.for_user(user)
    return Response({
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    })

@api_view(['GET'])
def is_authenticated(request):
    role = 'normal'
    if (request.user.is_superuser):
        role = 'admin'
    elif (request.user.is_staff):
        role = 'staff'
    return Response({'is_authenticated': request.user.is_authenticated,'role': role, 'username': request.user.username, 'email': request.user.email})

