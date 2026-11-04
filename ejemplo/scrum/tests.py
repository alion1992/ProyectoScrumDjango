from django.test import TestCase
from datetime import date

from .models import Tarea, Etiqueta, Sprint, Programador

# Create your tests here.

class TareaTest(TestCase):

    def setUp(self):
        # Creamos los datos necesarios para las pruebas

        self.programador = Programador.objects.create(
            nombre="Francisco", apellido1="Alia"
        )

        self.proyecto = Programador.objects.create(nombre = "Proyecto Prueba")

        self.sprint = Sprint.objects.create(
            fecha_inicio=date(2027,1,1)
        )

    def test_suma(self):
        resultado = 2 + 3

        self.assertEqual(resultado, 5)

    def test_crear_tarea(self):
        tarea = Tarea.objects.create(
            nombre="Desarrollar el login",
            fecha_inicio=date(2026, 10, 28),
            completa=False,
            sprint=self.sprint,
            programador=self.programador
        )
        self.assertEqual(tarea.nombre, "Desarrollar el login")
        self.assertFalse(tarea.completa)
        self.assertEqual(tarea.sprint, self.sprint)
        self.assertEqual(tarea.programador, self.programador)

    def test_crear_tarea_api(self):
        datos = {
            "nombre": "Desarrollar el login",
            "fecha_inicio": "2026-10-28",
            "fecha_fin": None,
            "completa": False,
            "sprint_id": self.sprint.id,
            "programador_id": self.programador.id,
            "etiquetas": ["Backend", "SQL"]
        }

        respuesta = self.client.post(
            "/api/crearTarea/",
            data=datos,
            content_type="application/json"
        )

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Tarea.objects.count(), 1)

    def test_crear_tarea_api2(self):
        datos = {
            "nombre": "Desarrollar el login",
            "fecha_inicio": "2026-10-28",
            "fecha_fin": None,
            "completa": False,
            "sprint_id": self.sprint.id,
            "programador_id": self.programador.id,
            "etiquetas": ["Backend", "SQL"]
        }

        respuesta = self.client.post(
            "/api/crearTarea/",
            data=datos,
            content_type="application/json"
        )

        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(Tarea.objects.count(), 1)