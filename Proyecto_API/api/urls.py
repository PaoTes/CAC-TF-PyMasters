from django.urls import path
from .views import index
from .views import ProductosView

urlpatterns = [
    path('', index, name='index'),
    path('productos/', ProductosView.as_view(), name='productos_list'),
    path('productos/<int:id>', ProductosView.as_view(), name='productos_process'),
    path('productos/nuevo/', ProductosView.as_view(), name='productos_nuevo'),
    path('productos/editar/<int:id>', ProductosView.as_view(), name='productos_editar'),
    path('productos/borrar/<int:id>', ProductosView.as_view(), name='productos_borrar'),
]