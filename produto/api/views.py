from rest_framework import generics
from produto.models import Produto, Catalogo
from . import serializers


class ListarCatalogos(generics.ListAPIView):
    queryset = Catalogo.objects.all()
    serializer_class = serializers.CatalogoSerializer


class ListarProdutos(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer


class DetalheProduto(generics.RetrieveAPIView):
    queryset = Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
    lookup_field = 'pk'


class ListarProdutoPorCatalogo(generics.ListAPIView):
    serializer_class = serializers.ProdutoSerializer

    def get_queryset(self):
        busca = self.kwargs['categoria']
        return Produto.objects.filter(catalogo=busca)