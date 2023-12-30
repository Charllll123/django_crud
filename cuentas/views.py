from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    forms = UserCreationForm()
    
    forms = {'forms': forms}
    
    return render(request, 'register/register.html', forms) 