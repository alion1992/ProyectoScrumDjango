from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida, name="bienvenida"),
    path('listarTareas/', views.listar_tareas,name="listar_tareas"),
    path('listarTarea/<int:id>', views.listar_tarea,name="listar_tarea"),
    path('listarTareaMejorado/<int:id>',views.listar_tarea_mejorado,name="listar_tarea_mejorado"),
    path('crearTarea/',views.crear_tarea,name="crear_tarea"),
    path('crearProgramador/',views.crear_programador,name="crear_programador")
]