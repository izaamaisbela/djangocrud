from django.shortcuts import render
from ..models import *

def home(request):
    user = CustomUser.objects.all()
    return render(request, 'home.html', {'usuarios': user})

def CriarUser(request):
    return render(request, 'criar_usuario.html')

def login(request):
    return render(request, 'login.html')