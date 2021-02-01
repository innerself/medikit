from django.contrib.auth import get_user_model
from django.test import TestCase

from medikit import utils
from .management.commands import generate_medicines as mgmt_generate_medicines
from .models import Kit, Medication

TEST_KIT_NAME = 'Test kit'


class TestUtils(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username='Vasya',
            email='qwe@asd.ru',
            password='s0me-cool-p@ss',
        )
        Kit.objects.create(
            name='Without kit',
            user=self.user,
        )

    def test_generate_medicines(self):
        utils.generate_medicines(kit_name=TEST_KIT_NAME)
        self.assertEquals(len(Kit.objects.all()), 1)
        self.assertEquals(len(Medication.objects.all()), 15)

        utils.generate_medicines(kit_name=TEST_KIT_NAME, quantity=3)
        self.assertEquals(len(Kit.objects.all()), 1)
        self.assertEquals(len(Medication.objects.all()), 18)

    def test_create_example_stuff(self):
        utils.create_example_stuff(self.user)
        # TODO What to check?


class TestManagementCommands(TestCase):

    def test_generate_medicines(self):
        mgmt_generate_medicines.Command().handle(kit_name=TEST_KIT_NAME)
