from django.db import models


class CategoriaModel(models.Model):
    categoria = models.CharField("Categoria" , max_length=100)

    def __str__(self):
        return self.categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['categoria']


class ProdutoModel(models.Model):
    produto = models.CharField('Nome Produto', max_length=100)
    preco = models.DecimalField('Preço Produto',max_digits=5, decimal_places=2)
    quantidade = models.IntegerField('Quantidade Produto')
    descricao = models.CharField("Descriçao do produto", max_length=200, null=True, blank=True)
    imagem = models.ImageField(upload_to='files')
    categoria = models.ForeignKey(CategoriaModel , related_name= 'categorias')

    def __str__(self):
        return self.produto

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['produto']