from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutAction, name='logout'),
    path('venda', views.venda, name='venda'),
    path('servicos', views.servicos, name='servicos'),
    path('clientes', views.clientes, name='clientes'),
    path('falecidos', views.falecidos, name='falecidos'),
]