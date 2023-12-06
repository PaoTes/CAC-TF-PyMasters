from django.urls import path
from .views import ProductosView
from . import views

urlpatterns = [
     path('', views.index, name='index'),
    path('productos/', ProductosView.as_view(), name='productos_list'),
    path('productos/<int:id>', ProductosView.as_view(), name='productos_process'),
]