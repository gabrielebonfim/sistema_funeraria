from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=255)
    sobrenome = models.CharField('Sobrenome', max_length=255)
    cpf = models.CharField('CPF', max_length=11)
    email = models.CharField('E-mail', max_length=255)
    telefone = models.CharField('Telefone', max_length=11)
    endereco = models.CharField('Endereço', max_length=255)
    data_cadastro = models.DateTimeField('Data de cadastro',auto_now_add=True)
    
    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class Servico(models.Model):
    nome = models.CharField('Nome do serviço', max_length=255)
    preco = models.DecimalField('Preço do serviço', decimal_places=2, max_digits=10)
    data_cadastro = models.DateTimeField('Data de cadastro',auto_now_add=True)
    
    def __str__(self):
        return f'{self.nome} (R$ {self.preco})'


class Falecido(models.Model):
    nome = models.CharField('Nome', max_length=255)
    sobrenome = models.CharField('Sobrenome', max_length=255)
    rg = models.CharField('RG', max_length=11)
    cpf = models.CharField('CPF', max_length=11)
    data_ncto = models.DateField('Data de Nascimento')
    data_obito = models.DateField('Data do Óbito')
    data_cadastro = models.DateTimeField('Data de cadastro',auto_now_add=True)
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome} ({self.data_ncto} – {self.data_obito})'


class Venda(models.Model):
    FORMPAG_CHOICES = (
        ('CC', 'Cartão de Crédito'),
        ('CD', 'Cartão de Débito'),
        ('D', 'Dinheiro'),
        ('T', 'Transferência (Entre contas/PIX)')
    )

    forma_pag = models.CharField('Forma de pagamento', max_length=2, choices=FORMPAG_CHOICES)
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente', on_delete=models.PROTECT)
    falecido = models.ForeignKey(Falecido, verbose_name='Falecido', on_delete=models.PROTECT)
    servicos = models.ManyToManyField(Servico, verbose_name='Serviços prestados')
    data_cadastro = models.DateTimeField('Data da venda',auto_now_add=True)
    valor_total = models.DecimalField('Valor total', decimal_places=2, max_digits=10)
    
    @property
    def valor_total():
        servicos = self.servicos.all()
        preco_total = 0.00
        for servico in servicos:
            preco_total += servico.preco
        return preco_total

    def __str__(self):
        return f'{self.id} - {self.cliente}'