from django.urls import path
from .views import *

urlpatterns = [
    path('task/', hola, name='tasks')
]
