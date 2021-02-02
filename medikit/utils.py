from dataclasses import dataclass

from django.contrib.auth import get_user_model
from mimesis import Food, Text, Datetime, Person

from .models import Kit, Medication


@dataclass
class ExampleMed:
    name: str
    description: str
    keep_in_cold: bool = False
    do_not_freeze: bool = False
    # TODO expires in some period after opening


EXAMPLE_STUFF = {
    'Example kit': [
        ExampleMed(
            name='Aspirin',
            description='Reduces pain, fever, or inflammation.',
        ),
        ExampleMed(
            name='Xymelin',
            description='Nasal drops',
        ),
        ExampleMed(
            name='Tetracycline',
            description='''
                    Therapeutic action
                    – Antibacterial
                    
                    Indications
                    – Treatment of bacterial conjunctivitis
                    – Treatment of trachoma (by preference use oral azithromycin for this indication)
                    – Prevention of neonatal conjunctivitis

                    ''',
            keep_in_cold=True,
        ),
    ],
    'Without kit': [
        ExampleMed(
            name='ACC Long',
            description='Used for loosening phlegm',
        ),
        ExampleMed(
            name='Paracetamol',
            description='''Used to treat pain and fever. 
            It is typically used for mild to moderate pain relief.''',
        ),
        ExampleMed(
            name='Tobradex',
            description='''This medication is used to treat or prevent eye 
            infections. This medication contains two drugs. Tobramycin belongs 
            to a class of drugs called aminoglycoside antibiotics. 
            It works by stopping the growth of bacteria. Dexamethasone 
            belongs to a class of drugs called corticosteroids. 
            It works by reducing swelling.
            
            This medication treats/prevents only bacterial eye infections. 
            It will not work for other types of eye infections. 
            Unnecessary use or overuse of any antibiotic can lead to 
            its decreased effectiveness.''',
            # TODO expires in some period after opening
        ),
    ]
}


def generate_medicines(kit_name: str, quantity: int = 15) -> None:
    kit = Kit.objects.filter(name=kit_name).first()

    if not kit:
        user = get_user_model().objects.create(username=Person().username())
        kit = Kit(name=kit_name, user=user)
        kit.save()

    print(f'Creating {quantity} fake medicines')

    for _ in range(quantity):
        Medication.objects.create(
            name=Food().fruit(),
            description=Text().title(),
            expiration_date=Datetime().date(start=2015, end=2025),
            kit=kit,
        )

    return None


def clear_kits() -> None:
    all_kits = Kit.objects.all()
    kits_quantity = len(all_kits)
    all_kits.delete()
    print(f'Deleted {kits_quantity} kits')

    return None


def clear_medicines() -> None:
    all_medicines = Medication.objects.all()
    medicines_quantity = len(all_medicines)
    all_medicines.delete()
    print(f'Deleted {medicines_quantity} medicines')

    return None


def clear_all() -> None:
    clear_medicines()
    clear_kits()


def create_example_stuff(user):
    example_kit = Kit.objects.create(name='Example kit', user=user)
    without_kit = Kit.objects.get(name='Without kit', user=user)

    for kit in (example_kit, without_kit):
        for medication in EXAMPLE_STUFF[kit.name]:
            Medication.objects.create(
                name=medication.name,
                description=medication.description,
                expiration_date=Datetime().date(start=2015, end=2025),
                # TODO Add 'keep_in_cold'
                kit=kit,
            )
