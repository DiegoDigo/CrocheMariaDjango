from rest_framework import serializers
from produto.models import CategoriaModel, ProdutoModel


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)

    class Meta:
        model = ProdutoModel
        fields = '__all__'

