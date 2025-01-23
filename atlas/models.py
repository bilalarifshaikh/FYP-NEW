# your_project/your_app/models.py

from django.db import models

#CODE BY BILAL FOR DATABASE RAW MATERIAL START
class RawMaterial(models.Model):
    MODEL_CHOICES = [
        ('420', '420'),
        ('428', '428'),
        ('CAM', 'CAM'),
    ]

    PART_CHOICES = [
        ('Inner Plate', 'Inner Plate'),
        ('Outer Plate', 'Outer Plate'),
        ('Pin', 'Pin'),
        ('Bush', 'Bush'),
        ('Roller', 'Roller'),
    ]

    MATERIAL_CHOICES = [
        ('SAE1050 (1.2 × 104.2)', 'SAE1050 (1.2 × 104.2)'),
        ('SAE1050 (1.2 × 1219)', 'SAE1050 (1.2 × 1219)'),
        ('SAE1050 (1.2 × 110.4)', 'SAE1050 (1.2 × 110.4)'),
        ('SAE1050 (1.5 × 111.3)', 'SAE1050 (1.5 × 111.3)'),
        ('SAE1050 (1.5 × 1219)', 'SAE1050 (1.5 × 1219)'),
        ('SAE1050 (1.5 × 115.7)', 'SAE1050 (1.5 × 115.7)'),
        ('SAE1045 (0.72 × 98)', 'SAE1045 (0.72 × 98)'),
        ('SAE1045 (0.72 × 1000)', 'SAE1045 (0.72 × 1000)'),
        ('SAE1045 (0.72 × 95.5)', 'SAE1045 (0.72 × 95.5)'),
        ('Steel Wire SCR420 (φ3.97)', 'Steel Wire SCR420 (φ3.97)'),
        ('Steel Wire SCR420 (φ4.51)', 'Steel Wire SCR420 (φ4.51)'),
        ('Steel Wire SAE1018 (φ5.00)', 'Steel Wire SAE1018 (φ5.00)'),
        ('Steel Wire SAE1018 (φ7.50)', 'Steel Wire SAE1018 (φ7.50)'),
        ('Steel Wire SAE1018 (φ6.03)', 'Steel Wire SAE1018 (φ6.03)'),
        ('Steel Wire SAE1018 (φ8.10)', 'Steel Wire SAE1018 (φ8.10)'),
        ('Steel Wire SCM420 (φ2.30)', 'Steel Wire SCM420 (φ2.30)'),
        ('Cold Rolled Steel SAE 8620 (0.435 × 4.72)', 'Cold Rolled Steel SAE 8620 (0.435 × 4.72)'),
    ]

    model = models.CharField(max_length=50, choices=MODEL_CHOICES)
    material = models.CharField(max_length=255, choices=MATERIAL_CHOICES)
    part = models.CharField(max_length=50, choices=PART_CHOICES)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.model} - {self.part} ({self.material})"

#CODE BY BILAL FOR DATABASE RAW MATERIAL END

class Production(models.Model):
    # Date field as primary key
    date = models.DateField(primary_key=True)

    # Choices for each field
    STAMPING_CHOICES = [
        ('420_inner', '420 inner'),
        ('420_outer', '420 outer'),
        ('428_inner', '428 inner'),
        ('428_outer', '428 outer'),
        ('cam_inner', 'cam inner'),
        ('cam_outer', 'cam outer'),
    ]

    COLD_FORMING_CHOICES = [
        ('420_bush', '420 bush'),
        ('420_roller', '420 roller'),
        ('428_bush', '428 bush'),
        ('428_roller', '428 roller'),
        ('cam_bush', 'cam bush'),
    ]

    PIN_CUTTING_CHOICES = [
        ('420_pin', '420 pin'),
        ('428_pin', '428 pin'),
        ('cam_pin', 'cam pin'),
    ]

    POLISHING_CHOICES = [
        ('420_inner', '420 inner'),
        ('420_outer', '420 outer'),
        ('428_inner', '428 inner'),
        ('428_outer', '428 outer'),
        ('cam_inner', 'cam inner'),
        ('cam_outer', 'cam outer'),
        ('420_pin', '420 pin'),
        ('428_pin', '428 pin'),
        ('cam_pin', 'cam pin'),
        ('420_bush', '420 bush'),
        ('420_roller', '420 roller'),
        ('428_bush', '428 bush'),
        ('428_roller', '428 roller'),
        ('cam_bush', 'cam bush'),
    ]

    DRYING_1_CHOICES = [
        ('cam_inner', 'cam inner'),
        ('cam_outer', 'cam outer'),
        ('cam_pin', 'cam pin'),
        ('cam_bush', 'cam bush'),
    ]

    DRYING_2_CHOICES = [
        ('420_inner', '420 inner'),
        ('420_outer', '420 outer'),
        ('428_inner', '428 inner'),
        ('428_outer', '428 outer'),
        ('420_pin', '420 pin'),
        ('428_pin', '428 pin'),
        ('420_bush', '420 bush'),
        ('420_roller', '420 roller'),
        ('428_bush', '428 bush'),
        ('428_roller', '428 roller'),
    ]

    AT_FURNACE_CHOICES = [
        ('420_inner', '420 inner'),
        ('420_outer', '420 outer'),
        ('428_inner', '428 inner'),
        ('428_outer', '428 outer'),
    ]

    CP_FURNACE_CHOICES = [
        ('cam_inner', 'cam inner'),
        ('cam_outer', 'cam outer'),
        ('420_pin', '420 pin'),
        ('428_pin', '428 pin'),
        ('cam_pin', 'cam pin'),
        ('420_bush', '420 bush'),
        ('420_roller', '420 roller'),
        ('428_bush', '428 bush'),
        ('428_roller', '428 roller'),
        ('cam_bush', 'cam bush'),
    ]

    SHOT_PEENING_CHOICES = [
        ('420_inner', '420 inner'),
        ('420_outer', '420 outer'),
        ('428_inner', '428 inner'),
        ('428_outer', '428 outer'),
    ]

    TUMBLER_POLISHING_CHOICES = [
        ('cam_inner', 'cam inner'),
        ('cam_outer', 'cam outer'),
        ('cam_pin', 'cam pin'),
        ('cam_bush', 'cam bush'),
    ]

    DRYING_CHOICES = [
        ('cam_inner', 'cam inner'),
        ('cam_outer', 'cam outer'),
        ('cam_pin', 'cam pin'),
        ('cam_bush', 'cam bush'),
    ]

    # Process fields with associated quantities
    stamping = models.CharField(max_length=255, choices=STAMPING_CHOICES)
    stamping_quantity = models.IntegerField()

    cold_forming = models.CharField(max_length=255, choices=COLD_FORMING_CHOICES)
    cold_forming_quantity = models.IntegerField()

    pin_cutting = models.CharField(max_length=255, choices=PIN_CUTTING_CHOICES)
    pin_cutting_quantity = models.IntegerField()

    polishing = models.CharField(max_length=255, choices=POLISHING_CHOICES)
    polishing_quantity = models.IntegerField()

    drying_1 = models.CharField(max_length=255, choices=DRYING_1_CHOICES)
    drying_1_quantity = models.IntegerField()

    drying_2 = models.CharField(max_length=255, choices=DRYING_2_CHOICES)
    drying_2_quantity = models.IntegerField()

    at_furnace = models.CharField(max_length=255, choices=AT_FURNACE_CHOICES)
    at_furnace_quantity = models.IntegerField()

    cp_furnace = models.CharField(max_length=255, choices=CP_FURNACE_CHOICES)
    cp_furnace_quantity = models.IntegerField()

    shot_peening = models.CharField(max_length=255, choices=SHOT_PEENING_CHOICES)
    shot_peening_quantity = models.IntegerField()

    tumbler_polishing = models.CharField(max_length=255, choices=TUMBLER_POLISHING_CHOICES)
    tumbler_polishing_quantity = models.IntegerField()

    drying = models.CharField(max_length=255, choices=DRYING_CHOICES)
    drying_quantity = models.IntegerField()

    def __str__(self):
        return f"Production on {self.date}"


# your_project/your_app/models.py

class Targets(models.Model):
    # Date field for the target
    date = models.DateField(primary_key=True)

    # Target fields for each process
    _420_target = models.IntegerField()
    _428_target = models.IntegerField()
    cam_target = models.IntegerField()

    def __str__(self):
        return f"Targets for {self.date}"
