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
def productoPorCategoria(request,categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    productos = objCategoria.producto_set.all()
    categorias = Categoria.objects.all()
    context = {
        "productos": productos,
        "categorias": categorias
        }
    return render(request,'index.html',context)

def productoPorNombre(request):
    nombre = request.POST['nombre']
    productos = Producto.objects.filter(nombre__contains=nombre)
    categorias = Categoria.objects.all()
    context = {
        "productos": productos,
        "categorias": categorias
        }
    return render(request,'index.html',context)
    