from django.core.management import BaseCommand

from medikit.utils import generate_drugs


class Command(BaseCommand):
    help = 'Generates random drugs for the given kit'

    def add_arguments(self, parser):
        parser.add_argument('kit_name', type=str)
        parser.add_argument('--quantity')

    def handle(self, *args, **options):
        if options.get('quantity'):
            generate_drugs(options['kit_name'], options['quantity'])
        else:
            generate_drugs(options['kit_name'])
