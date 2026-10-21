from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
