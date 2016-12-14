from django.db import models


class Catalogo(models.Model):
    nome = models.CharField("Nome Catalogo", max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Catalogo'
        verbose_name_plural = 'Catalogos'
        ordering = ['nome']


class ProdutoImagem(models.Model):
    imagens = models.ImageField(upload_to="files/detalhe", null=True, blank=True)

    def __str__(self):
        return str(self.imagens)

    class Meta:
        verbose_name = 'imagem'
        verbose_name_plural = 'imagens'


class ProdutoDetalhe(models.Model):
    descricao = models.TextField(null=True, blank=True)
    imagens = models.ForeignKey(ProdutoImagem, related_name="imagen")

    def __str__(self):
        return str(self.imagens)

    class Meta:
        verbose_name = 'Detalhe Produto'
        verbose_name_plural = 'Detalhes Produtos'


class Produto(models.Model):
    catalogo = models.ForeignKey(Catalogo, related_name="catalogo")
    nome = models.CharField('Nome Produto', max_length=100)
    descricao = models.TextField(null=True, blank=True)
    quantidade = models.IntegerField('Quantidade Produto')
    preco = models.DecimalField('Preço Produto',max_digits=6, decimal_places=2)
    slug = models.SlugField(max_length=150)
    imagem = models.ImageField(upload_to='files', blank=True, null=True)
    detalheProduto = models.ForeignKey(ProdutoDetalhe, related_name='detalhes')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']