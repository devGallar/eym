from django.shortcuts import redirect, render,get_object_or_404
from modelapp.carrito import Cart
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

def productoDetalle(request,producto_id):
    objProducto = get_object_or_404(Producto,pk=producto_id)
    context = {
        'producto':objProducto
    }
    return render(request,'producto.html',context)

def carrito(request):
    return render(request,'carrito.html')
def agregarCarrito(request,producto_id):
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
    else:
        cantidad = 1
    
    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,cantidad)
    
    
    if request.method == 'GET':
        return redirect('/')
    
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.delete(objProducto)
    
    return render(request,'carrito.html')

def limpiarCarrito(request):
    carritoProducto = Cart(request)
    carritoProducto.clear()
    
    return render(request,'carrito.html')
    