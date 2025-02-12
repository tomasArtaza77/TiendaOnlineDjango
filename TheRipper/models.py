from django.db import models

# Create your models here.
# En esta seccion creo las clases que seran las aplicaciones de mi proyecto. Esta 
# es mi estructura de mi base de datos.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30) 
   # apellido = models.CharField(max_length=30)  
    direccion = models.CharField(max_length=50, verbose_name="La direccion") 
    email = models.EmailField(blank=True, null=True) 
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre 


class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField() 

    def __str__(self): 
        return 'El nombre es %s, la seccion es %s y el precio es %s' % (self.nombre,self.seccion,self.precio) 




class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()  
