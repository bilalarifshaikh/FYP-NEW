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

class FinishedProduct(models.Model):
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

    model = models.CharField(max_length=50, choices=MODEL_CHOICES)
    part = models.CharField(max_length=50, choices=PART_CHOICES)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.model} - {self.part} ({self.quantity})"

class Priority420(models.Model):
    model = models.CharField(max_length=50, default="420")
    part = models.CharField(max_length=50)
    priority = models.IntegerField()

    def __str__(self):
        return f"{self.model} - {self.part} (Priority {self.priority})"
    
# Priority model for 428
class Priority428(models.Model):
    model = models.CharField(max_length=50, default="428")
    part = models.CharField(max_length=50)
    priority = models.IntegerField()

    def __str__(self):
        return f"{self.model} - {self.part} (Priority {self.priority})"

# Priority model for CAM
class PriorityCAM(models.Model):
    model = models.CharField(max_length=50, default="CAM")
    part = models.CharField(max_length=50)
    priority = models.IntegerField()

    def __str__(self):
        return f"{self.model} - {self.part} (Priority {self.priority})"

