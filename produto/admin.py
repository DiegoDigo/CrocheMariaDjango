from django.contrib import admin
from .models import Produto, Catalogo, ProdutoImagem , ProdutoDetalhe


#class AdminProduto(admin.ModelAdmin):
#    list_display = ['nome', 'quantidade', 'preco', 'catalogo', 'slug']


#admin.site.register(Produto, AdminProduto)
admin.site.register(Produto)
admin.site.register(Catalogo)
admin.site.register(ProdutoImagem)
admin.site.register(ProdutoDetalhe)


