# Generated by Django 3.2 on 2021-04-27 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('email', models.CharField(max_length=255, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Falecido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('rg', models.CharField(max_length=11, verbose_name='RG')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('data_ncto', models.DateField(verbose_name='Data de Nascimento')),
                ('data_obito', models.DateField(verbose_name='Data do Óbito')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do serviço')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço do serviço')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pag', models.CharField(choices=[('CC', 'Cartão de Crédito'), ('CD', 'Cartão de Débito'), ('D', 'Dinheiro'), ('T', 'Transferência (Entre contas/PIX)')], max_length=2, verbose_name='Forma de pagamento')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data da venda')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gerenciamento.cliente', verbose_name='Cliente')),
                ('falecido', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gerenciamento.falecido', verbose_name='Falecido')),
                ('servicos', models.ManyToManyField(to='gerenciamento.Servico', verbose_name='Serviços prestados')),
            ],
        ),
    ]
