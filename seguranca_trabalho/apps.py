from django.apps import AppConfig
from core import settings


class SegurancaTrabalhoConfig(AppConfig):
    name = 'seguranca_trabalho'
    verbose_name = "Segurança do trabalho"

    def ready(self):
        import sys
        from . import scheduler
        if (len(sys.argv) > 1 and sys.argv[1] == 'runserver'):
            if settings.SCHEDULER_AUTOSTART:
                scheduler.start()