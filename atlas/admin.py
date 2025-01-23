from django.contrib import admin
from .models import Production
from .models import Targets

# Register your models here.
admin.site.register(Production)
admin.site.register(Targets)
