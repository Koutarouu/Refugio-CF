from django.test import TestCase
from .models import Vacuna

# Create your tests here.
class VacunaTestCase(TestCase):
	def setUp(self):
		Vacuna.objects.create(nombre='influenza' )#ojo esto no se va a guardar en la BDD

	def test_mascotas_have_sexo(self):
		pedro = Vacuna.objects.get(nombre='influenza')

		self.assertEqual(pedro.nombre,'influenza')#se ejecuta con python manage.py test y a esto se le le llama un happytest
		#todas las pruebas las hace aqui