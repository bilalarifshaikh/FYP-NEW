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
def RenderDashboard(request):
    # Fetch quantities for the "420" model and its parts
    raw_materials = RawMaterial.objects.filter(model="420")
    quantities = {item.part: item.quantity for item in raw_materials}

    # Fetch total quantities for each model
    total_quantities = {
        '420': raw_materials.aggregate(total=Sum('quantity'))['total'] or 0,
        '428': RawMaterial.objects.filter(model='428').aggregate(total=Sum('quantity'))['total'] or 0,
        'CAM': RawMaterial.objects.filter(model='CAM').aggregate(total=Sum('quantity'))['total'] or 0,
    }

    return render(request, 'dashboard.html', {
        'quantities': quantities,
        'total_quantities': total_quantities,
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
    logout(request)
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

        # Check if a record already exists
        existing_material = RawMaterial.objects.filter(
            model=model, part=part, material=material
        ).first()

        if existing_material:
            # Increment the quantity if it exists
            existing_material.quantity += quantity
            existing_material.save()
            messages.success(
                request, f"Updated quantity of {material} by {quantity} units."
            )
        else:
            # Create a new record if it doesn't exist
            RawMaterial.objects.create(
                model=model, part=part, material=material, quantity=quantity
            )
            messages.success(request, "New raw material added successfully!")

        return redirect("raw_material")

    return render(request, "raw_material.html")