from django.core.management.base import BaseCommand
from atlas.models import FinishedProduct

class Command(BaseCommand):
    help = 'Deducts quantities from FinishedProduct entries'

    def handle(self, *args, **kwargs):
        # Deduction values based on your description
        deductions = {
            ('CAM', 'Bush'): 50,
            ('CAM', 'Pin'): 10,
            ('CAM', 'Outer Plate'): 20,
            ('CAM', 'Inner Plate'): 15,
            ('428', 'Roller'): 10,
            ('428', 'Bush'): 25,
            ('428', 'Pin'): 20,
            ('428', 'Outer Plate'): 30,
            ('428', 'Inner Plate'): 23,
            ('420', 'Roller'): 13,
            ('420', 'Bush'): 11,
            ('420', 'Pin'): 23,
            ('420', 'Outer Plate'): 30,
            ('420', 'Inner Plate'): 23
        }

        for (model, part), deduction in deductions.items():
            # Fetch the FinishedProduct record for the given model and part
            try:
                product = FinishedProduct.objects.get(model=model, part=part)
                # Apply the deduction
                if product.quantity >= deduction:
                    product.quantity -= deduction
                    product.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully deducted {deduction} from {model} - {part}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Not enough quantity for {model} - {part} to deduct'))
            except FinishedProduct.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'{model} - {part} does not exist in the database'))
