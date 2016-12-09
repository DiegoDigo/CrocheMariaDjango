from django.contrib import admin
from .models import ClienteModel, EnderecoModel


class AdminCliente(admin.ModelAdmin):
    list_display = ['nome', 'endereco']


class AdminEndereco(admin.ModelAdmin):
    list_display = ['cidade', 'estado', 'bairro', 'logradouro', 'logradouroNumero']

admin.site.register(ClienteModel, AdminCliente)
admin.site.register(EnderecoModel, AdminEndereco)