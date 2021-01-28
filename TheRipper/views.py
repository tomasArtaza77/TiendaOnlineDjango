from TheRipper.models import Articulos
from django.http.response import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from TheRipper.forms import formularioContacto 

# Create your views here.


def busqueda_productos(request):
    return render(request, "busqueda_produ.html")
#
def buscar(request):

    if request.GET["prd"]:
        #mensaje="Artículo buscado:%r" %request.GET["prd"]  
        producto=request.GET["prd"]

        if len(producto)>20:
            mensaje="Busqueda demasiada larga."
            
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto) 
            return render(request,"resultados_busqueda.html",{"articulos":articulos,"query":producto})   

    else:
        mensaje="No pusiste nada" 
    return HttpResponse(mensaje)


def contacto(request):
    if request.method == "POST":

        miFormulario = formularioContacto(request.POST)  

        if miFormulario.is_valid():
            infoFormulario = miFormulario.cleaned_data 
            send_mail(infoFormulario['asunto'], infoFormulario['mensaje'], 
            infoFormulario.get('email',''),['artaza.tomas_17@yahoo.com'],)   

            return render(request, "gracias.html") 
    else:
        miFormulario = formularioContacto() 
    
    return render(request, "formulario_contacto.html", {"form": miFormulario})  
