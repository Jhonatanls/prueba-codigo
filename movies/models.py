from django.db import models

class Genero(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Indice_madurez(models.Model):
    name = models.CharField(max_length=6)

    def __str__(self):
        return self.name
    
class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    genero = models.ManyToManyField(Genero)
    calificacion = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    cantidad_vistas = models.IntegerField()
    argumento = models.CharField(max_length=255)
    actor = models.ManyToManyField(Actor)
    duracion = models.IntegerField()
    fecha_publicacion = models.DateField()
    indice_madurez = models.ManyToManyField(Indice_madurez)
    imagen_cartelera = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo}({self.calificacion}) - {self.argumento} "