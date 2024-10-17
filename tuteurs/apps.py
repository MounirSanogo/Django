from django.apps import AppConfig


class TuteursConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tuteurs'

#profil des tuteurs

class EtudiantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tuteurs'

    def ready(self):
        import tuteurs.signals  # Importer vos signaux

