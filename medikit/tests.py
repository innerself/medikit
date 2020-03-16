from django.test import TestCase

from .models import Kit, Drug
from .utils import generate_drugs


class TestUtils(TestCase):

    def test_generate_drugs(self):
        generate_drugs(kit_name='Test')
        self.assertEquals(len(Kit.objects.all()), 1)
        self.assertEquals(len(Drug.objects.all()), 15)

        generate_drugs(kit_name='Test', quantity=3)
        self.assertEquals(len(Kit.objects.all()), 1)
        self.assertEquals(len(Drug.objects.all()), 18)
