from decouple import config
from django.test import TestCase

from .management.commands import generate_drugs as mgmt_generate_drugs
from .models import Kit, Drug
from .utils import generate_drugs


class TestUtils(TestCase):

    def test_generate_drugs(self):
        generate_drugs(kit_name=config('TEST_KIT_NAME'))
        self.assertEquals(len(Kit.objects.all()), 1)
        self.assertEquals(len(Drug.objects.all()), 15)

        generate_drugs(kit_name=config('TEST_KIT_NAME'), quantity=3)
        self.assertEquals(len(Kit.objects.all()), 1)
        self.assertEquals(len(Drug.objects.all()), 18)


class TestManagementCommands(TestCase):

    def test_generate_drugs(self):
        mgmt_generate_drugs.Command().handle(kit_name=config('TEST_KIT_NAME'))
