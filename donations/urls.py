from django.urls import path
from .views import *

urlpatterns = [
    path('donate/',donation,name='donate'),
]