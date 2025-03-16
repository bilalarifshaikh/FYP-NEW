from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
import logging, random, string
from reportlab.lib.pagesizes import letter
from .models import *
from django.db import transaction
from django.contrib import messages
from .models import RawMaterial
from django.template.loader import render_to_string
from django.db.models import Sum
import logging, random
from reportlab.platypus import Paragraph, Spacer
import datetime, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
from reportlab.pdfgen import canvas
from django.db import transaction
from django.core.exceptions import ValidationError
from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle



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

def ShowRawMaterial(request):
    context = {}
    context['Products'] = RawMaterial.objects.all().order_by('-id')
    return render(request, 'AllProducts.html', context)
def ShowFinishedMat(request):
    context = {}
    context['Products'] = FinishedProduct.objects.all().order_by('-id')
    return render(request, 'AllFinished.html', context)
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from .models import FinishedProduct
from datetime import datetime

def finished_products(request):
    products = FinishedProduct.objects.all()
    return render(request, 'finished_products/product_table.html', {'Products': products})

def download_pdf(request):
    # Query the FinishedProduct model
    products = FinishedProduct.objects.all()

    # Create an HttpResponse object to serve the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="finished_products_report.pdf"'

    # Create a PDF using ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Create the styles for the document
    styles = getSampleStyleSheet()

    # Define custom styles for title and headings
    title_style = styles['Title']
    title_style.fontName = 'Helvetica-Bold'
    title_style.fontSize = 20
    title_style.alignment = 1  # Center-aligned

    heading_style = styles['Heading1']
    heading_style.fontName = 'Helvetica-Bold'
    heading_style.fontSize = 16
    heading_style.alignment = 1  # Center-aligned

    body_style = styles['BodyText']
    body_style.fontName = 'Helvetica'
    body_style.fontSize = 12
    body_style.alignment = 1  # Center-aligned

    # Create custom paragraph style for centered text
    centered_style = ParagraphStyle(
        'Centered',
        parent=styles['Normal'],
        alignment=1,  # Center-aligned
        fontName='Helvetica',
        fontSize=12
    )

    content = []

    content.append(Spacer(1, 10))

    content.append(
        Paragraph('<img src="static/images/logo.jpg" width="140" height="100"/>', centered_style)
    )
    content.append(Spacer(1, 20))

    # Add company name and report title with centered alignment
    content.append(
        Paragraph("<b>ATLAS D.I.D ASSEMBLY REPORT</b>", title_style)
    )
    content.append(
        Paragraph("<b>Finished Products Report</b>", heading_style)
    )
    content.append(
        Paragraph("Date: " + datetime.now().strftime('%Y-%m-%d'), body_style)
    )

    # Add a line break
    content.append(Spacer(1, 12))

    # Add logo at the top (centered)
    # content.append(
    #     Spacer(1, 20)  # Space between title and logo
    # )
    

    # Add another line break for spacing
    content.append(Spacer(1, 12))

    # Define the table data
    table_data = [['MODEL', 'PART', 'QUANTITY(Kgs)']]  # Header Row

    # Add the product data to the table
    for product in products:
        table_data.append([product.model, product.part, str(product.quantity)])

    # Create the table with borders
    # table = Table(table_data, colWidths=[doc.width/4.0] * 3)
    table = Table(table_data, colWidths=[doc.width / 3, doc.width / 3, doc.width / 3])  # Columns span equally


    # Style the table
    table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header background color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center-align all content
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font style
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Body font style
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding in the header row
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Table grid lines (borders)
        ('FONTSIZE', (0, 0), (-1, -1), 12),  # Font size for the entire table (adjust as needed)
        ('ROWHEIGHT', (0, 0), (-1, -1), 20),  # Row height for increased spacing between rows
    ]))

    # Add the table to the content
    content.append(table)

    # Build the document
    doc.build(content)

    return response

    # # Query the FinishedProduct model
    # products = FinishedProduct.objects.all()

    # # Create an HttpResponse object to serve the PDF
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="finished_products_report.pdf"'

    # # Create a PDF using ReportLab
    # p = canvas.Canvas(response, pagesize=letter)
    # width, height = letter

    # # Add company logo (optional)
    # p.drawImage('static/images/logo.jpg', 50, height - 100, width=100, height=80)

    # # Add company name and report title
    # p.setFont("Helvetica-Bold", 20)
    # p.drawString(200, height - 50, "ATLAS D.I.D ASSEMBLY PLANT")
    # p.setFont("Helvetica-Bold", 20)
    # p.drawString(200, height - 100, "Finished Products Report")
    # p.setFont("Helvetica", 10)
    # p.drawString(450, height - 120, "Date: " + datetime.now().strftime('%Y-%m-%d'))

    # # Add table headers
    # p.drawString(50, height - 150, "MODEL")
    # p.drawString(150, height - 150, "PART")
    # p.drawString(250, height - 150, "Quantity")

    # # Add product data
    # y_position = height - 180
    # for product in products:
    #     p.drawString(50, y_position, product.model)
    #     p.drawString(150, y_position, product.part)
    #     p.drawString(250, y_position, str(product.quantity))
    #     y_position -= 20

    # # Save the PDF and return the response
    # p.showPage()
    # p.save()

    # return response
# Render the graphs page
def graphs(request):
    return render(request, 'graph.html')

def download_pdf2(request):
    # Query the FinishedProduct model
    products = RawMaterial.objects.all()

    # Create an HttpResponse object to serve the PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="raw_materia;_report.pdf"'

    # Create a PDF using ReportLab
    doc = SimpleDocTemplate(response, pagesize=letter)

    # Create the styles for the document
    styles = getSampleStyleSheet()

    # Define custom styles for title and headings
    title_style = styles['Title']
    title_style.fontName = 'Helvetica-Bold'
    title_style.fontSize = 20
    title_style.alignment = 1  # Center-aligned

    heading_style = styles['Heading1']
    heading_style.fontName = 'Helvetica-Bold'
    heading_style.fontSize = 16
    heading_style.alignment = 1  # Center-aligned

    body_style = styles['BodyText']
    body_style.fontName = 'Helvetica'
    body_style.fontSize = 12
    body_style.alignment = 1  # Center-aligned

    # Create custom paragraph style for centered text
    centered_style = ParagraphStyle(
        'Centered',
        parent=styles['Normal'],
        alignment=1,  # Center-aligned
        fontName='Helvetica',
        fontSize=12
    )

    content = []

    content.append(Spacer(1, 10))

    content.append(
        Paragraph('<img src="static/images/logo.jpg" width="140" height="100"/>', centered_style)
    )
    content.append(Spacer(1, 20))

    # Add company name and report title with centered alignment
    content.append(
        Paragraph("<b>ATLAS D.I.D</b>", title_style)
    )
    content.append(
        Paragraph("<b>Raw Materials Report</b>", heading_style)
    )
    content.append(
        Paragraph("Date: " + datetime.now().strftime('%Y-%m-%d'), body_style)
    )

    # Add a line break
    content.append(Spacer(1, 12))

    # Add logo at the top (centered)
    # content.append(
    #     Spacer(1, 20)  # Space between title and logo
    # )
    

    # Add another line break for spacing
    content.append(Spacer(1, 12))

    # Define the table data
    table_data = [['MODEL', 'PART', 'MATERIAL', 'QUANTITY(Kgs)']]  # Header Row

    # Add the product data to the table
    for product in products:
        table_data.append([product.model, product.part, product.material, str(product.quantity)])

    # Create the table with borders
    table = Table(table_data, colWidths=[doc.width / 4, doc.width / 4, doc.width / 2, doc.width / 4])  # Columns span equally

    # Style the table
    table.setStyle(TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        # ('WORDWRAP', (0, 0), (-1, -1), True)  # Enable word wrap for text in cells
        # ('ALIGN', (0, 0), (-1, -1), 'CENTER')
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center-align all content
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Header font style
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Body font style
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Padding in the header row
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Table grid lines (borders)
        ('FONTSIZE', (0, 0), (-1, -1), 12),  # Font size for the entire table (adjust as needed)
        ('ROWHEIGHT', (0, 0), (-1, -1), 20),  # Row height for increased spacing between rows
    ]))

    # Add the table to the content
    content.append(table)

    # Build the document
    doc.build(content)

    return response

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