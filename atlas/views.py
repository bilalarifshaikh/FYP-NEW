from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
import logging, random, string
from .models import RawMaterial
from django.db import transaction
from django.contrib import messages
from .models import RawMaterial
from django.db.models import Sum
import logging, random, string
import datetime, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from django.db import transaction
from django.core.exceptions import ValidationError

# BOM dictionary (replace with your existing BOM)
BOM = {
    "420": {
        "Inner Plate": {"SAE1050 (1.2 × 104.2)": 249.95, "SAE1050 (1.2 × 1219)": 249.95},
        "Outer Plate": {"SAE1050 (1.2 × 110.4)": 189.14, "SAE1050 (1.2 × 1219)": 189.14},
        "Pin": {"Steel Wire SCR420 (φ3.97)": 149.59},
        "Bush": {"Steel Wire SAE1018 (φ5.00)": 109.75},
        "Roller": {"Steel Wire SAE1018 (φ7.50)": 161.42},
    },
    "428": {
        "Inner Plate": {"SAE1050 (1.5 × 111.3)": 394.17, "SAE1050 (1.5 × 1219)": 394.17},
        "Outer Plate": {"SAE1050 (1.5 × 115.7)": 314.42, "SAE1050 (1.5 × 1219)": 314.42},
        "Pin": {"Steel Wire SCR420 (φ4.51)": 228.15},
        "Bush": {"Steel Wire SAE1018 (φ6.03)": 149.45},
        "Roller": {"Steel Wire SAE1018 (φ8.10)": 234.52},
    },
    "CAM": {
        "Inner Plate": {"SAE1045 (0.72 × 98)": 40.48, "SAE1045 (0.72 × 1000)": 40.48},
        "Outer Plate": {"SAE1045 (0.72 × 95.5)": 33.18, "SAE1045 (0.72 × 1000)": 33.18},
        "Pin": {"Steel Wire SCM420 (φ2.30)": 23.60},
        "Bush": {"Cold Rolled Steel SAE 8620 (0.435 × 4.72)": 13.62},
    },
}


# Creating login logic and interface
def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        pswd = request.POST['password']
        user = authenticate(username=username, password=pswd)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            return redirect('Show Dashboard')  # Redirect to the dashboard
        else:
            # If not, return to login page again
            messages.error(request, "Incorrect username and/or password.")
            return render(request, 'login.html')
    return render(request, 'login.html')

# Code by Hamna
# Render the dashboard and fetch quantities for 420 parts and total quantities for each model
def calculate_production(bom, raw_materials):
    """
    Calculate how many parts and complete chains can be produced based on raw materials.
    """
    parts_production = {}
    for part, materials in bom.items():
        min_production = float('inf')
        
        # Combine stocks for replacement materials
        combined_stock = 0
        for material, qty_required in materials.items():
            available_stock = raw_materials.get(material.strip(), 0)  # Normalize material name
            combined_stock += available_stock

        # Calculate possible units for this part using combined stock
        for material, qty_required in materials.items():
            possible_units = combined_stock // qty_required
            min_production = min(min_production, possible_units)

        parts_production[part] = int(min_production)  # Total parts possible
    return parts_production


def RenderDashboard(request):
    # Fetch raw material stock from the database
    raw_materials = RawMaterial.objects.values('material').annotate(total=Sum('quantity'))
    raw_materials_dict = {item['material'].strip(): item['total'] for item in raw_materials}

    # Debugging: Print normalized raw materials stock
    print("Normalized Raw Materials Stock:", raw_materials_dict)

    # Calculate production for each model
    production = {}
    for model, bom in BOM.items():
        parts_production = calculate_production(bom, raw_materials_dict)
        complete_chains = min(parts_production.values()) if parts_production else 0  # Bottleneck part determines chains
        production[model] = {
            "parts": parts_production,
            "chains": complete_chains,
        }

    # Debugging: Print production data
    print("Production Data:", production)

    return render(request, 'dashboard.html', {
        'production': production,
    })
# Code by Hamna


# Render the At Furnace page
def AtFurnace(request):
    return render(request, 'at_furnace.html')

# Render the graphs page
def graphs(request):
    return render(request, 'graph.html')

# Log out the user
def logout_view(request):
    # logout(request)
    return redirect('login')  # Redirect to the login page after logout

# Render the display page
def display(request):  
    return render(request, "display.html")

# Render the targets page
def targets(request):
    return render(request, "targets.html")

# Render the Cp Furnace page
def CpFurnace(request):
    return render(request, "cp_furnace.html")
# def raw_material(request):
#     return render(request, "raw_material.html")
def raw_material(request):
    if request.method == "POST":
        model = request.POST.get("model")
        part = request.POST.get("part")
        material = request.POST.get("material")
        quantity = request.POST.get("quantity")

        # Validate inputs
        if not (model and part and material and quantity):
            messages.error(request, "All fields are required!")
            return redirect("raw_material")

        try:
            quantity = int(quantity)
            if quantity <= 0:
                messages.error(request, "Quantity must be greater than zero.")
                return redirect("raw_material")
        except ValueError:
            messages.error(request, "Quantity must be a valid number.")
            return redirect("raw_material")

        # Check if the material already exists
        existing_material = RawMaterial.objects.filter(
            model=model, part=part, material=material
        ).first()

        if existing_material:
            # Increment quantity
            existing_material.quantity += quantity
            existing_material.save()
            messages.success(request, f"Updated quantity of {material} by {quantity} units.")
        else:
            # Create new material record
            RawMaterial.objects.create(
                model=model, part=part, material=material, quantity=quantity
            )
            messages.success(request, "New raw material added successfully!")

        return redirect("raw_material")

    return render(request, "raw_material.html")