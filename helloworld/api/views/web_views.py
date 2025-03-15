from django.shortcuts import render, redirect
from ..models import *

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
        
    user = CustomUser.objects.all()
    return render(request, 'home.html', {'usuarios': user})

def criarUser(request, id=None):
    if id:
        usuario = CustomUser.objects.filter(id=id).first()
        
    if usuario:
        return render(request, 'criar_user.html', {'usuarios': usuario})

    else:
         return redirect('usuario')


def login(request):
    return render(request, 'login.html')