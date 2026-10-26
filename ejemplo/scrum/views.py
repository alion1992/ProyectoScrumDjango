from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Tarea
import json


def inicio(request):
    return HttpResponse("Bienvenido a mi aplicación Django")

def listar_tareas(request):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Método no permitido"},
            status=405
        )

    tareas = Tarea.objects.values()

    return JsonResponse(list(tareas), safe=False)

def listar_tarea_concreta(request,id):
    if request.method != "GET":
        return JsonResponse(
            {"error": "Método no permitido"},
            status=405
        )
    tarea = Tarea.objects.filter(id=id).values().first()
    return JsonResponse(tarea)

@csrf_exempt
def crear_tarea(request):
    if request.method == "POST":
        return JsonResponse(
            {"error": "Método no permitido"},
            status=405
        )

