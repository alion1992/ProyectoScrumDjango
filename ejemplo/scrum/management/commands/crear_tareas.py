
from django.core.management import BaseCommand
from ...models import Tarea, Etiqueta, Programador


class Command(BaseCommand):
    help = "Este comando va a crear tareas de prueba"

    def handle(self, *args, **options):

        try:
            #CREACION DE ETIQUETA
            etiqueta = Etiqueta(nombre='tiene programador')
            etiqueta.save()
            self.stdout.write(self.style.SUCCESS(f"SE HA GUARDADO LA ETIQUETA CORRECTAMENTE"))
            #CREACION DE PROGRAMADOR
            programador = Programador(nombre='Francisco',apellido1='Alia')
            programador.save()

            #CREACION DE TAREA
            tarea = Tarea(nombre='Tarea con programador',programador=programador)
            tarea.save()
            tarea.etiquetas.add(etiqueta)

            self.stdout.write(self.style.SUCCESS(f"La tarea con nombre: {tarea.nombre} se ha insertado correctamente"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"{e}"))