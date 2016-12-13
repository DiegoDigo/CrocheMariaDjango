from django.contrib import admin
from .models import Pedido , Status , PedidoItem

admin.site.register(Pedido)
admin.site.register(PedidoItem)
admin.site.register(Status)
