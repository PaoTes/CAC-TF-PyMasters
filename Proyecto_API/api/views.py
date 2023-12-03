from typing import Any
from django import http
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views import View
from .models import Productos
import _json
import json

class ProductosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request,id=0):
        if (id>0):
            productos=list(Productos.objects.filter(id=id).values())
            if len(productos) > 0:
                producto=productos[0]
                datos={'message':"Success",'producto':producto}
            else:
                datos={'message':"Product not found"}
            return JsonResponse(datos)
        
        else:
            productos=list(Productos.objects.values())
            if len(productos)>0:
                datos={'message':"Success",'productos':productos}
            else:
                datos={'message':"Products not found"}
            return JsonResponse(datos)
            

    def post(self, request):
       #print(request.body)
       jd=json.loads(request.body)
       #print(jd)
       Productos.objects.create(Nombre=jd['Nombre'],Descripcion=jd['Descripcion'],Marca=jd['Marca'])
       datos={'message':"Success"}
       return JsonResponse(datos)


    def put(self, request,id):
        jd=json.loads(request.body)
        productos=list(Productos.objects.filter(id=id).values())
        if len(productos)>0:
            producto=Productos.objects.get(id=id)
            producto.Nombre=jd['Nombre']
            producto.Descripcion=jd['Descripcion']
            producto.Marca=jd['Marca']
            producto.save()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Product not found"}
        return JsonResponse(datos)

    def delete(self, request,id):
        productos=list(Productos.objects.filter(id=id).values())
        if len(productos)>0:
            Productos.objects.filter(id=id).delete()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Product not found"}
        return JsonResponse(datos)
