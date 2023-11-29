from django.shortcuts import render
from modelapp.models import *



def index(request):
    productos = Producto.objects.all();
    context = {"productos": productos}
    return render(request,'index.html',context)