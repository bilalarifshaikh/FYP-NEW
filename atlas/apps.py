# Code by Hamna
from django.apps import AppConfig

class AtlasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'atlas'
# Code by Hamna

    def ready(self):
        from .scheduler import start_scheduler
        start_scheduler()

#code by Bilal