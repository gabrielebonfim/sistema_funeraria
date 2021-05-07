from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, forms
from gerenciamento.models import *
import os
from django.core.exceptions import ValidationError
from django import forms

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "sobrenome", "cpf", "email", "telefone", "endereco"]

class FalecidoForm(ModelForm):
    class Meta:
        model = Falecido
        fields = ["nome", "sobrenome", "cpf", "data_ncto", "data_obito"]

class ServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = ["nome", "preco"]


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ["forma_pag", "cliente", "falecido", "servicos"]