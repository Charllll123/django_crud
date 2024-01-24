from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def register(request):

    if request.method == 'GET':
        forms = UserCreationForm()

        forms = {'forms': forms}

        return render(request, 'register/register.html', forms)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                messages.success(request, 'Usuario creado')
                login(request, user)
                return redirect('home')
            except:
                messages.error(request, 'Este usuario ya exciste ')
                return redirect('cuenta')
        else:
            return HttpResponse('La contraseña no coincide')

def salir(request):
    logout(request)
    return redirect('home')        

def entrar(request):
    
    if request.method == 'POST':
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            message = messages.error(request, 'Username o Password es incorrecto')
            forms = AuthenticationForm()
            return render(request, 'register/login.html', {'forms': forms, 'menssage': message})
        else:
            login(request, user)
            return redirect('tasks')    
    else:
        forms = AuthenticationForm()
        
        return render(request, 'register/login.html', {'forms': forms})
