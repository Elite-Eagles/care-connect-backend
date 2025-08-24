from django.urls import path
from .views import *

urlpatterns = [
    path('', disaster_list, name='disaster-list'),
    path('add/', disaster_create, name='disaster-create'),
]