from django.db import models

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio= models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre
