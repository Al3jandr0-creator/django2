from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    nota = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.nota}"