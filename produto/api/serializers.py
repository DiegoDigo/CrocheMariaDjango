from rest_framework import serializers
from produto import models


class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Catalogo
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    catalogo = CatalogoSerializer(read_only=True)

    class Meta:
        model = models.Produto
        fields = '__all__'

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProdutoImagem
        fields = '__all__'


class DetalheProdutoSerializer(serializers.ModelSerializer):
    imagens = ImagenSerializer(read_only=True)

    class Meta:
        model = models.ProdutoDetalhe
        fields = '__all__'

class DetalheDoProdutoSerializer(serializers.ModelSerializer):

    detalheProduto = DetalheProdutoSerializer(read_only=True)
    catalogo = CatalogoSerializer(read_only=True)

    class Meta:
        model = models.Produto
        fields = '__all__'