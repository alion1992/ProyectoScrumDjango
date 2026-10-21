

# Create your models here.
from django.db import models



class Programador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido1 = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} {self.nombre}"

class Proyecto(models.Model):
    nombre  = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id} {self.nombre}"

class Sprint(models.Model):

    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True,blank=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"{self.id} {self.fecha_inicio}"


class Etiqueta(models.Model):
    nombre  = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} {self.nombre}"

class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField(null=True,blank=True)
    fecha_fin = models.DateField(null=True,blank=True)
    completa = models.BooleanField(default=False)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE,null=True,blank=True)
    programador = models.ForeignKey(Programador, on_delete=models.CASCADE,null=True,blank=True)
    etiquetas = models.ManyToManyField(Etiqueta,null=True,blank=True)

    def __str__(self):
        return f"[{self.nombre}]" + ", ".join([e.nombre for e in self.etiquetas.all()])

