import os
import django

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atlas.settings")

# Initialize Django
django.setup()

# Import your models after initializing Django
from atlas.models import RawMaterial

# Fetch all raw materials from the database
db_materials = RawMaterial.objects.values_list('material', flat=True)
# BOM for each model
BOM = {
    "420": {
        "Inner Plate": {"SAE1050 1.2 × 104.2": 249.95, "SAE1050 1.2 × 1219": 249.95},
        "Outer Plate": {"SAE1050 1.2 × 110.4": 189.14, "SAE1050 1.2 × 1219": 189.14},
        "Pin": {"Steel Wire SCR420 φ3.97": 149.59},
        "Bush": {"Steel Wire SAE1018 φ5.00": 109.75},
        "Roller": {"Steel Wire SAE1018 φ7.50": 161.42},
    },
    "428": {
        "Inner Plate": {"SAE1050 1.5 × 111.3": 394.17, "SAE1050 1.5 × 1219": 394.17},
        "Outer Plate": {"SAE1050 1.5 × 115.7": 314.42, "SAE1050 1.5 × 1219": 314.42},
        "Pin": {"Steel Wire SCR420 φ4.51": 228.15},
        "Bush": {"Steel Wire SAE1018 φ6.03": 149.45},
        "Roller": {"Steel Wire SAE1018 φ8.10": 234.52},
    },
    "CAM": {
        "Inner Plate": {"SAE1045 0.72 × 98": 40.48, "SAE1045 0.72 × 1000": 40.48},
        "Outer Plate": {"SAE1045 0.72 × 95.5": 33.18, "SAE1045 0.72 × 1000": 33.18},
        "Pin": {"Steel Wire SCM420 φ2.30": 23.60},
        "Bush": {"Cold Rolled Steel Sheet SAE 8620 0.435 × 4.72": 13.62},
    },
}
# BOM materials
bom_materials = []
for model, parts in BOM.items():
    for part, materials in parts.items():
        bom_materials.extend(materials.keys())

# Check for discrepancies
missing_in_db = [material for material in bom_materials if material not in db_materials]
if missing_in_db:
    print("Materials in BOM but not in DB:", missing_in_db)
else:
    print("All BOM materials match the database.")
