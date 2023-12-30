from django.urls import path
from .views import *

urlpatterns = [
    path('cuenta/', register, name = 'register'),
]
