from django.urls import path
from . import views

urlpatterns = [
    path('hola/', views.inicio, name="inicio"),
    path('tareas/', views.listar_tareas, name="tareas"),
    path('tarea/<int:id>',views.listar_tarea_concreta,name="tarea"),
    path('crearTarea/',views.crear_tarea,name="crear_tarea")
]