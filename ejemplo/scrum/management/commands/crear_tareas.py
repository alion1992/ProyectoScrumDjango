
from django.core.management import BaseCommand
from ...models import Tarea, Etiqueta
class Command(BaseCommand):
    help = "Este comando va a crear tareas de prueba"

    def handle(self, *args, **options):

        try:
            #CREACION DE ETIQUETA
            etiqueta = Etiqueta(nombre='1245')
            etiqueta.save()
            self.stdout.write(self.style.SUCCESS(f"SE HA GUARDADO LA ETIQUETA CORRECTAMENTE"))
            #CREACION DE TAREA
            tarea = Tarea(nombre='Tarea ponte ya')
            tarea.save()
            tarea.etiquetas.add(etiqueta)

            self.stdout.write(self.style.SUCCESS(f"La tarea con nombre: {tarea.nombre} se ha insertado correctamente"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"{e}"))