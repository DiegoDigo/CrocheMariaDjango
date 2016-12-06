from django.contrib import admin
from .models import Produto, Preco, Imagem

admin.site.register(Preco)
admin.site.register(Produto)
admin.site.register(Imagem)
