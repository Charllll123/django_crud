from django.urls import path
from .views import *

urlpatterns = [
    path('cuenta/', register, name = 'cuenta'),
    path('salir/', salir, name='salir'),
    path('entrar/', entrar, name='entrar' )
]
