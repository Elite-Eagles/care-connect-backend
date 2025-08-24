from django.urls import path
from .views import *

urlpatterns = [
    path('become/',become_volunteer,name='become-volunteer'),
    path('help-requests/',get_help_requests,name='help-requests'),
    path ('resources/',get_resources,name='resources'),
]