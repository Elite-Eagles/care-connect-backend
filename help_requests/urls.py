from django.urls import path
from .views import *

urlpatterns = [
    path('create/',help_request_create,name='help-request-create'),
    path('list/',user_help_request,name='help-request-list'),
    path('all/',all_help_requests,name='all-help-requests'),
]