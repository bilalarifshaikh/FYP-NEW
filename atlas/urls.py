"""
URL configuration for atlas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name="display"),
    path('login/', views.login_request, name="login"),
    path('Targets/', views.targets, name="targets"),
    path('Dashboard/', views.RenderDashboard, name="homepage"),
    path('Dashboard/', views.RenderDashboard, name="Show Dashboard"),
    path('payorder/', views.RenderDashboard, name="Payorder"),
    path('receiveit/', views.RenderDashboard, name="Receive It"),
    path('package/<int:package_id>/', views.RenderDashboard, name="package_details"),
    path('ShowAllpackages/', views.RenderDashboard, name="All Packages"),
    path('ShowAllProducts/', views.RenderDashboard, name="All Products"),
    path('ShowAllLogistics/', views.RenderDashboard, name="All Logistics"),
    path('DispatchPack/<int:package_id>/', views.RenderDashboard , name='Dispatch Package'),
    path('EditProduct/<int:product_id>/', views.RenderDashboard , name='Edit Product'),
    path('EditLogistics/<int:logistic_id>/', views.RenderDashboard , name='Edit Logistics'),
    path('AtFurnace/', views.AtFurnace , name='at_furnace'),
    path('CpFurnace/', views.CpFurnace , name='cp_furnace'),
    path('AddLogistics/', views.RenderDashboard, name="Add Logistics"),
    path('Dashboard/', views.RenderDashboard, name="Show Dashboard"),
    path('logout/', views.logout, name="Logout"),
    path('graph/', views.graphs, name="graphs"),
    path('raw_material/', views.raw_material, name="raw_material"),
]
