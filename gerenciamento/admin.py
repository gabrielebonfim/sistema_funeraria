from django.contrib import admin

from .models import *

admin.site.register(Cliente)
admin.site.register(Servico)
admin.site.register(Falecido)
admin.site.register(Venda)