from django.db import models

# Create your models here.

class Restaurantes(models.Model):

    nombre = models.CharField(max_length= 60)
    especialidad = models.CharField(max_length= 100)
    locacion = models.CharField(max_length= 100)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    breve_descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='media/images/', null=True, blank=True)

    def __str__(self):
        return f'Nombre: {self.nombre}, Especialidad:{self.especialidad}, Locacion: {self.locacion}'

class Bares(models.Model):

    nombre = models.CharField(max_length= 60)
    especialidad = models.CharField(max_length= 100)
    locacion = models.CharField(max_length= 100)
    horario_apertura = models.TimeField()
    horario_cierre = models.TimeField()
    breve_descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='media/images/', null=True, blank=True)

    def __str__(self):
        return f'Nombre: {self.nombre}, Especialidad:{self.especialidad}, Locacion: {self.locacion}'
