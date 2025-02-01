from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
import logging, random, string
#from .models import *
from django.db import transaction
from django.contrib import messages
import datetime, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage

#creating login logic and interface
def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        pswd = request.POST['password']
        user = authenticate(username=username, password=pswd)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)                              #IDHAR AAO
            #fetch dashboard data for dashboard.html
            return redirect('Show Dashboard')
        else:
            # If not, return to login page again
            messages.error(request, "Incorrect username and/or password.")
            return render(request, 'login.html')
    return render(request, 'login.html')

def RenderDashboard(request):
    return render(request, 'dashboard.html')

def AtFurnace(request):
    return render(request, 'at_furnace.html')

def graphs(request):
    return render(request, 'graph.html')
def logout(request):
    return render(request, 'login.html')
def display(request):
    return render(request, "display.html")
def targets(request):
    return render(request, "targets.html")
def CpFurnace(request):
    return render(request, "cp_furnace.html")
def raw_material(request):
    return render(request, "raw_material.html")