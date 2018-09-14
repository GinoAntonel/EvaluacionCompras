from django.conf.urls import url
from .views import dame_compras, mostrar, eliminar, archivar

urlpatterns = [
    url(r'^$', dame_compras, name='index'),
    url(r'^compras$', mostrar),
    url(r'^eliminar$', eliminar),
    url(r'^archivar$', archivar),   
]