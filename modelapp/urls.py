from django.urls import path
from . import views




app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('productosPorCategoria/<int:categoria_id>',views.productoPorCategoria,name='productosPorCategoria'),
    path('productosPorNombre>',views.productoPorNombre,name='productosPorNombre')
    
]
