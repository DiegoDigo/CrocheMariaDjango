from rest_framework import serializers
from produto.models import Produto, Catalogo, ProdutoDetalhe


class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalogo
        fields = '__all__'


class ProdutoDetalheSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProdutoDetalhe
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    catalogo = CatalogoSerializer(read_only=True)
    produto = ProdutoDetalheSerializer(read_only=True)
    class Meta:
        model = Produto
        fields = '__all__'




