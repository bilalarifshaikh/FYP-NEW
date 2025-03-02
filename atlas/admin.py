from django.contrib import admin
from .models import RawMaterial
from .models import FinishedProduct

# Register your models here.
admin.site.register(RawMaterial)
admin.site.register(FinishedProduct)
