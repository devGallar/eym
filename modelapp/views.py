from django.shortcuts import render
from modelapp.models import *



def index(request):
    productos = Producto.objects.all();
    categorias = Categoria.objects.all();
    context = {
        "productos": productos,
        "categorias": categorias
        }
    return render(request,'index.html',context)