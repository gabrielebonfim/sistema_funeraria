from django.shortcuts import render, redirect
from datetime import datetime
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from descansodepaz.forms import *
from .models import *

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
    return redirect('index')


def venda(request):
    clientes = Cliente.objects.all()
    falecidos = Falecido.objects.all()
    servicos = Servico.objects.all()

    if request.method == 'POST':
        form = VendaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Venda efetuada com sucesso')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Preencha os campos corretamente!')

    return render(request,'venda.html',  {'clientes': clientes, 'falecidos':falecidos, 'servicos':servicos})


def cadastros(request):
    return render(request,'cadastros.html')


def relatorios(request):
    return render(request,'index.html')


def clientes(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente cadastrado com sucesso')
            return redirect('falecidos')
        else:
            messages.warning(request, 'Preencha os campos corretamente!')

    return render(request,'clientes.html')

def servicos(request):
    servicos = Servico.objects.all()

    if request.method == 'POST':
        form = ServicoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Servico cadastrado com sucesso')
            return redirect('venda')
        else:
            messages.warning(request, 'Preencha os campos corretamente!')

    return render(request,'servicos.html', {'servicos': servicos})


def falecidos(request):
    if request.method == 'POST':
        form = FalecidoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f'Falecido cadastrado com sucesso')
            return redirect('servicos')
        else:
            messages.warning(request, 'Preencha os campos corretamente!')

    return render(request,'falecidos.html')