from django.contrib import admin
from .models import Produto, Preco, Imagem, Tipo


class AdminImagem(admin.ModelAdmin):
    list_display = ['tipo', 'imagen']


class AdminProduto(admin.ModelAdmin):
    list_display = ['tipo', 'imagen']


class AdminPreco(admin.ModelAdmin):
    list_display = ['precoUnitario', 'precoPacote']


class AdminTipo(admin.ModelAdmin):
    list_display = ['tipo']

admin.site.register(Preco)
admin.site.register(Produto)
admin.site.register(Imagem, AdminImagem)
admin.site.register(Tipo, AdminTipo)
