from django.db import models
from cliente.models import ClienteModel
from produto.models import ProdutoModel


class Status(models.Model):
    statusPedido = (
        ('aberto','Aberto'),
        ('cancelado','Cancelado'),
        ('finalizado','Finalizado'),
    )
    status = models.CharField('Status ', choices=statusPedido , default='aberto',max_length=10)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering = ['status']


class Pedido(models.Model):
    data = models.DateTimeField(auto_now=False , auto_now_add=False)
    cliente = models.ForeignKey(ClienteModel, related_name='clientes')
    valorPedido = models.DecimalField("Valor total Pedido", max_digits=5, decimal_places=2)
    status = models.ForeignKey(Status, default=1)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['data']


class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='pedidos')
    produto = models.ForeignKey(ProdutoModel, related_name='produtos')
    produtoName = models.CharField("Nome Produto", max_length=100)
    quantidadeItens = models.PositiveIntegerField("quantidade itens")
    valorUnitario = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.produtoName

    class Meta:
        verbose_name = 'PedidoItem'
        verbose_name_plural = 'PedidosItens'
        ordering = ['produtoName']