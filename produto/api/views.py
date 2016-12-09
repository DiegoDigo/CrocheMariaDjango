from rest_framework import generics
from produto.models import ProdutoModel , CategoriaModel
from . import  serializers


class ListarCategorias(generics.ListAPIView):
    queryset = CategoriaModel.objects.all()
    serializer_class = serializers.CategoriaSerializer


class ListarProdutos(generics.ListAPIView):
    queryset = ProdutoModel.objects.all()
    serializer_class = serializers.ProdutoSerializer


class DetalheProduto(generics.RetrieveAPIView):
    queryset = ProdutoModel.objects.all()
    serializer_class = serializers.ProdutoSerializer
    lookup_field = 'pk'


class ListarProdutoPorCategoria(generics.ListAPIView):
    serializer_class = serializers.ProdutoSerializer

    def get_queryset(self):
        busca = self.kwargs['categoria']
        return ProdutoModel.objects.filter(categoria=busca)