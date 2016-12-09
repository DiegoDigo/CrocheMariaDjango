from django.contrib import admin
from .models import ProdutoModel, CategoriaModel


class AdminProduto(admin.ModelAdmin):
    list_display = ['produto', 'quantidade', 'preco', 'categoria']


class AdminCategoria(admin.ModelAdmin):
    list_display = ['id', 'categoria']

admin.site.register(ProdutoModel, AdminProduto)
admin.site.register(CategoriaModel, AdminCategoria)

