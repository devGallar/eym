from django.shortcuts import render
from modelapp.models import *

def verProductos(request):
    productos = Producto.objects.all();
    dict = {"productos": productos}
    return render(request,"verproductos.html",dict)

def frmCompra(request, id):
    producto = Producto.objects.get(id=id)  
    dict = {"producto": {
        "nombre": producto.nombre,
            "imagen_url": producto.imagen.url,
            "precio": producto.precio,
            "stock": producto.stock,
            "descripcion": producto.descripcion,
            "categoria": producto.categoria.nombre
    }}

    return render(request, "frmcompra.html", dict)