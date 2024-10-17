from django.apps import AppConfig


class EtudiantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'etudiants'

#profil des etudiants
class EtudiantsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'etudiants'

    def ready(self):
        import etudiants.signals  # Importer vos signaux
