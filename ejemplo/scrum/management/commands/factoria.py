from faker import Faker
from datetime import date
import random
from django.core.management import BaseCommand
from ...models import *
class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        try:
            faker = Faker('es_ES')
            #Creacion de programadores
            for i in range(10):
                programador = Programador(nombre = faker.name(),apellido1= faker.last_name())
                programador.save()

            #Creacion de proyecto
            proyecto = Proyecto(nombre='Proyecto DAW2')
            proyecto.save()

            #Creacion de sprint
            for i in range(4):
                sprint = Sprint(fecha_inicio=date.today(),proyecto=proyecto)

            for i in range(30):
                programadores = Programador.objects.all()
                tarea = Tarea(nombre=faker.name_nonbinary(), programador= random.choice(programadores),fecha_inicio=date.today())
                tarea.save()

            self.stdout.write(self.style.SUCCESS(f"Se ha creado la factoria correctamente"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Se ha producido un error {e}"))
