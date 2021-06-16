from django.apps import AppConfig
from core import settings


class SegurancaTrabalhoConfig(AppConfig):
    name = 'seguranca_trabalho'
    verbose_name = "Segurança do trabalho"

    def ready(self):
        from . import scheduler
        if settings.SCHEDULER_AUTOSTART:
        	scheduler.start()