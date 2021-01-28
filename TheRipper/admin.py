from django.contrib import admin
from TheRipper.models import Clientes, Articulos, Pedidos 

# Register your models here.

class clientesAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","telefono","email")  #lo que quiero mostrar  
    search_fields=("nombre","telefono") #barra de busqueda


class articulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",)  #barra de filtros

class pedidosAdmin(admin.ModelAdmin):
    list_display=("numero","fecha") 
    list_filter=("fecha",) 
    date_hierarchy=("fecha") #muestro horizontal el campo que quiero filtrar   


admin.site.register(Clientes, clientesAdmin) 
admin.site.register(Articulos, articulosAdmin) 
admin.site.register(Pedidos, pedidosAdmin)  

