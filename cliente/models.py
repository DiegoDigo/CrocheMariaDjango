from django.conf import settings
from django.db import models


class EnderecoModel(models.Model):
    logradouro = models.CharField('Rua', max_length=100)
    logradouroNumero = models.CharField('Número', max_length=5)
    bairro = models.CharField('Bairro', max_length=100)
    cep = models.CharField('cep', max_length=8)
    cidade = models.CharField('cidade', max_length=100)
    estado = models.CharField('Estado', max_length=100)
    siglaEstado = models.CharField('Sigla Estado', max_length=2)

    def __str__(self):
        return self.logradouro

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['cidade']


class ClienteModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    nome = models.CharField("Nome Cliente", max_length=100)
    endereco = models.ForeignKey(EnderecoModel, related_name='endereços')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']
