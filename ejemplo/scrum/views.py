from json import JSONDecodeError

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Tarea, Etiqueta, Sprint, Programador
import json

def bienvenida(request):
    return HttpResponse("Hola chicos e Inmaculada estamos en nuestro primer controlador")

def listar_tareas(request):
    if request.method != "GET":
        return JsonResponse("Error esta peticion solo funciona con get")

    tareas = Tarea.objects.all().values()

    return JsonResponse(list(tareas),safe=False)

def listar_tarea(request,id):
    if request.method != "GET":
        return JsonResponse("Error esta peticion solo funciona con get")

    tarea = Tarea.objects.get(id=id)
    datos ={
        "id": tarea.id,
        "nombre": tarea.nombre,
        "fecha_inicio": (
            tarea.fecha_inicio.isoformat()
            if tarea.fecha_inicio else None
        ),
        "fecha_fin": (
            tarea.fecha_fin.isoformat()
            if tarea.fecha_fin else None
        ),
        "completa": tarea.completa,
        "sprint_id": tarea.sprint_id,
        "programador_id": tarea.programador_id,
    }
    return JsonResponse(datos)


def listar_tarea_mejorado(request,id):
    if request.method != "GET":
        return JsonResponse("Error esta peticion solo funciona con get")

    tarea = Tarea.objects.filter(id=id).values().first()

    return JsonResponse(tarea)


@csrf_exempt
def crear_tarea(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Tipo de petición no es correcta'},status=405)
    try:
        tarea_json = json.loads(request.body)
    except JSONDecodeError as e:
        return JsonResponse({'error': 'El Json no esta bien formado'},status=400)

    #VALIDACIONES
    if not Sprint.objects.filter(id=tarea_json.get("sprint_id")).exists():
        return JsonResponse({
            'error': 'El sprint indicado no existe'
        }, status=404)

    # Comprobamos que existe el programador
    if not Programador.objects.filter(id=tarea_json.get("programador_id")).exists():
        return JsonResponse({
            'error': 'El programador indicado no existe'
        }, status=404)

    #Aqui hacemos el save del objeto tarea de nuestro model
    tarea = Tarea.objects.create(
        nombre = tarea_json.get("nombre"),
        fecha_inicio = tarea_json.get("fecha_inicio"),
        fecha_fin = tarea_json.get("fecha_fin"),
        completa = tarea_json.get("completa",False),
        sprint_id = tarea_json.get("sprint_id"),
        programador_id = tarea_json.get("programador_id")
    )

    # SI EN LA TAREA VIENEN ETIQUETAS Y ESAS ETIQUETAS NO EXISTEN, QUIERO QUE LA GUARDES
    etiquetas = tarea_json.get("etiquetas", [])
    crear_etiquetas(etiquetas,tarea)

    return JsonResponse({'exito': 'Se ha creado correctamente la tarea',
                         'tarea': tarea.id})


@csrf_exempt
def crear_programador(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Tipo de petición no es correcta'},status=405)
    try:
        programador_json = json.loads(request.body)
    except JSONDecodeError as e:
        return JsonResponse({'error': 'El Json no esta bien formado'},status=400)

    programador = Programador.objects.create(
        nombre = programador_json.get("nombre"),
        apellido1 = programador_json.get("apellido1")
    )
    etiquetas = programador_json.get("etiquetas", [])
    crear_etiquetas(etiquetas, programador)

    return JsonResponse({'exito': 'Se ha creado correctamente el programador',
                         'tarea': programador.id})


def crear_etiquetas(etiquetas,objeto):

        for etiqueta in etiquetas:
            etiquita_model, creada = Etiqueta.objects.get_or_create(nombre=etiqueta)
            objeto.etiquetas.add(etiquita_model)
            if not creada:
                print("Se ha creada la etiqueta")
            else:
                print("Etiqueta Nueva")




'''
@csrf_exempt
def crear_tarea(request):
    if request.method != "POST":
        return JsonResponse({'error' : 'Operación no permitida'},status=405)
    else:
        try:
            tarea = json.loads(request.body)
        except JSONDecodeError as e:
            return JsonResponse({'error' : 'Error al decodificar el json'},status=400)
    nueva_tarea = Tarea.objects.create(
        nombre=tarea["nombre"],
        fecha_inicio=tarea.get("fecha_inicio"),
        fecha_fin=tarea.get("fecha_fin"),
        completa=tarea.get("completa", False),
        sprint_id=tarea.get("sprint_id"),
        programador_id=tarea.get("programador_id")
    )
    return JsonResponse(
        {
            "mensaje": "Tarea creada correctamente",
            "id": nueva_tarea.id
        },
        status=201
    )


'''






'''def inicio(request):
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
'''
