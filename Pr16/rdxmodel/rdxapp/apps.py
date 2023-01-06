from django.apps import AppConfig


class RdxappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rdxapp'

    def ready(self):
        import rdxapp.signals
