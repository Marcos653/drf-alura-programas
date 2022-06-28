from django.test import TestCase
from aluraflix.models import Programa


class FixtureDataTestCase(TestCase):
    fixtures = ['programas_iniciais']

    def test_verifica_load(self):
        programa_bizarro = Programa.objects.get(pk=1)
        all_programas = Programa.objects.all()
        self.assertEqual(programa_bizarro.titulo, 'Coisas bizarras')
        self.assertEqual(len(all_programas), 9)
