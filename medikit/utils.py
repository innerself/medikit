from mimesis import Food, Text, Datetime
from .models import Kit, Medication


def generate_drugs(kit_name: str, quantity: int = 15) -> None:
    kit = Kit.objects.filter(name=kit_name).first()

    if not kit:
        kit = Kit(name=kit_name)
        kit.save()

    print(f'Creating {quantity} fake drugs')

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


def clear_drugs() -> None:
    all_drugs = Medication.objects.all()
    drugs_quantity = len(all_drugs)
    all_drugs.delete()
    print(f'Deleted {drugs_quantity} drugs')

    return None


def clear_all() -> None:
    clear_drugs()
    clear_kits()
