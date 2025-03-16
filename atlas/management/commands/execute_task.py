from django.core.management.base import BaseCommand
from atlas.models import FinishedProduct
from django.db import transaction
from atlas.models import *


class Command(BaseCommand):
    help = 'Deducts quantities from FinishedProduct entries'
    # In a separate Python script or Django management command


# def calculate_and_store_priorities():
    


    def handle(self, *args, **kwargs):
        # Define the quantities required for each part to make one chain (420 model)
        requirements_420 = {
            'Inner Plate': 142.47,
            'Outer Plate': 121.08,
            'Pin': 140.33,
            'Bush': 88.91,
            'Roller': 106.05
        }

        # Step 1: Fetch available quantities from the FinishedProduct table
        available_420 = {}
        for part in requirements_420.keys():
            try:
                product = FinishedProduct.objects.get(model='420', part=part)
                available_420[part] = product.quantity
            except FinishedProduct.DoesNotExist:
                available_420[part] = 0  # Default to 0 if part is not found

        # Step 2: Calculate the number of full chains we can make for each part
        full_chains = {}
        for part, required_quantity in requirements_420.items():
            available_quantity = available_420.get(part, 0)
            full_chains[part] = available_quantity // required_quantity  # Full chains = available / required

        # Step 3: Find the remaining quantity of each part
        remaining_parts = {}
        for part, full_chain_count in full_chains.items():
            required_quantity = requirements_420[part]
            remaining_parts[part] = available_420[part] - (full_chain_count * required_quantity)

        # Step 4: Sort parts by remaining quantity to assign priorities
        sorted_parts = sorted(remaining_parts.items(), key=lambda x: x[1])  # Sort by remaining quantity, ascending

        # Step 5: Assign priorities (smallest remaining quantity gets Priority 1)
        priorities = []
        priority = 1
        for part, remaining_quantity in sorted_parts:
            priorities.append({
                'model': '420',
                'part': part,
                'priority': priority
            })
            priority += 1

        # Step 6: Store the priorities in the Priority420 table
        # Using a transaction to ensure atomicity
        with transaction.atomic():
            # Clear existing priorities for model '420' (if any)
            Priority420.objects.filter(model='420').delete()

            # Insert the new priorities
            for priority_info in priorities:
                Priority420.objects.create(
                    model=priority_info['model'],
                    part=priority_info['part'],
                    priority=priority_info['priority']
                )

        print("Priorities for 420 model have been successfully calculated and stored.")
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
