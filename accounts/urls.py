from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('firebase-login/',firebase_login_view, name='firebase_login'),
    path('signup/',signup_view, name='signup'),
    path('is-authenticated/',is_authenticated,name='is-authenticated'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]