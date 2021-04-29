from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from descansodepaz.forms import *

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    else:
        form = UsuarioForm()

        if request.method == 'POST':
            form = UsuarioForm(request.POST)

            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Bem-vindo {user}, seu cadastro foi criado com sucesso!')
                return redirect('login')

            else:
                messages.warning(request, 'Preencha os campos corretamente!')

    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')

            else:
                messages.warning(request, 'Usuario OU senha invalidos!')

    return render(request,'login.html')


def logoutAction(request):
    logout(request)
    return redirect('login')


def venda(request):
    return render(request,'index.html')


def cadastros(request):
    return render(request,'index.html')

def relatorios(request):
    return render(request,'index.html')

def clientes(request):
    return render(request,'index.html')


def servicos(request):
    return render(request,'index.html')

def falecidos(request):
    return render(request,'index.html')