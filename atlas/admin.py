from django.contrib import admin
from .models import RawMaterial
from .models import FinishedProduct
from .models import Priority420
from .models import *

# Register your models here.
admin.site.register(RawMaterial)
admin.site.register(FinishedProduct)
admin.site.register(Priority420)
admin.site.register(Priority428)
admin.site.register(PriorityCAM)

