from django.contrib import admin
from .models import RawMaterial
from .models import FinishedProduct
from .models import Priority420

# Register your models here.
admin.site.register(RawMaterial)
admin.site.register(FinishedProduct)
admin.site.register(Priority420)