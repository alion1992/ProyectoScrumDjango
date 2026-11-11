from collections import Counter

from django.test import TestCase
from .models import Tarea, Etiqueta, Sprint, Programador
from datetime import date

class TareaTest(TestCase):

    def setUp(self):
        self.programador = Programador.objects.create(
            nombre="Francisco"
        )

        self.sprint = Sprint.objects.create(
            fecha_inicio=date(2026,11,9)
        )

    def test_num_sprint(self):
        sprint = Sprint.objects.count()
        self.assertEqual(sprint,1)

    def test_crear_sprint(self):
        Sprint.objects.create(
            fecha_inicio=date(2026, 12, 9)
        )
        self.assertEqual(Sprint.objects.count(),2)


    def test_suma(self):
        resultado = 4 + 4
        self.assertEqual(resultado, 8)
        self.assertEqual(Sprint.objects.count(), 1)


    def test_resta(self):
        resultado = 10 - 5
        self.assertEqual(resultado, 5)

    def test_comparacion(self):
        comprobacion = True
        nombre = "Francisco"
        nombre2 = "francisco"
        if nombre.strip().lower() != nombre2:
            comprobacion = False
        self.assertTrue(comprobacion)

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

    def test_crear_tarea_con_sprint_que_no_existe(self):
        datos = {

            "fecha_inicio": "2026-10-28",
            "fecha_fin": None,
            "completa": False,
            "sprint_id": 3,
            "programador_id": self.programador.id,
            "etiquetas": ["Backend", "SQL"]
        }

        respuesta = self.client.post(
            "/api/crearTarea/",
            data=datos,
            content_type="application/json"
        )

        self.assertEqual(respuesta.status_code, 404)
        self.assertEqual(Tarea.objects.count(), 0)