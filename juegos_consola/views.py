from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from .models import Console, Retrojuego 

def consolas(request):
    if request.user.is_authenticated:
        consolas = Console.objects.all()

        return render(request, 'juegos_consola/listado.html', {'consolas': consolas})
    else:
        return redirect('login')