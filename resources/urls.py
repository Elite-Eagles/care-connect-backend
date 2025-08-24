from django.urls import path
from .views import *

urlpatterns = [
    path('add/',resource_create,name='add-resource'),
    path('get-nearby-resources/',get_nearby_resources,name='get-nearby-resources')
]