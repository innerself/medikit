from django.test import TestCase

from .management.commands import generate_medicines as mgmt_generate_medicines
from .models import Kit, Medication
from .utils import generate_medicines

TEST_KIT_NAME = 'Test kit'


class TestUtils(TestCase):

    def test_generate_medicines(self):
        generate_medicines(kit_name=TEST_KIT_NAME)
        self.assertEquals(len(Kit.objects.all()), 1)
        self.assertEquals(len(Medication.objects.all()), 15)

        generate_medicines(kit_name=TEST_KIT_NAME, quantity=3)
        self.assertEquals(len(Kit.objects.all()), 1)
        self.assertEquals(len(Medication.objects.all()), 18)


class TestManagementCommands(TestCase):

    def test_generate_medicines(self):
        mgmt_generate_medicines.Command().handle(kit_name=TEST_KIT_NAME)
