from django.db import models


class Imagem(models.Model):
    imagen = models.ImageField(null=True, blank=True, upload_to='files')
    tipo = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.tipo)

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
        ordering = ['tipo']


class Preco(models.Model):
    precoUnitario = models.DecimalField(max_digits=5,decimal_places=2)
    precoPacote = models.DecimalField(max_digits=5,decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.precoUnitario)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'
        ordering = ['precoUnitario']


class Tipo(models.Model):
    tipo = models.CharField("Tipo Produto", max_length=100)

    def __str__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['tipo']


class Produto(models.Model):
    descProduto = models.CharField("Descrição Produto", max_length=100)
    tipo = models.ForeignKey(Tipo)
    preco = models.ForeignKey(Preco)
    cor = models.CharField("Cor Produto", max_length=100)
    imagens = models.ForeignKey(Imagem)

    def __str__(self):
        return self.descProduto

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['descProduto']
