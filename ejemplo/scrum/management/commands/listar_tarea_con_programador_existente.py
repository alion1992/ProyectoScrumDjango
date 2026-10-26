from django.core.management import BaseCommand
from ...models import Tarea,Programador



class Command(BaseCommand):
    help = ""

    def handle(self, *args, **options):
        programador = Programador.objects.get(pk=1)
        tarea = Tarea(nombre='Tarea con programador existe', programador=programador)
        tarea.save()
        self.stdout.write(self.style.SUCCESS(f"Se ha insertado correctamente la tarea"))
