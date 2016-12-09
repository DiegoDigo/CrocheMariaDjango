from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^produtos/$', views.ListarProdutos.as_view()),
    url(r'^produto/(?P<pk>[0-9]+)/$', views.DetalheProduto.as_view()),
    url(r'^categorias/$', views.ListarCategorias.as_view()),
    url(r'^produto/categoria/(?P<categoria>[0-9]+)/$', views.ListarProdutoPorCategoria.as_view()),
]
