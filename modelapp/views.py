from django.shortcuts import render
from modelapp.models import *

def verProductos(request):
    productos = Producto.objects.all();
    dict = {"productos": productos}
    return render(request,"verproductos.html",dict)
