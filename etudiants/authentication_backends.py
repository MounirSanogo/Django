from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Utilisation du modèle utilisateur par défaut de Django
        UserModel = get_user_model()
        try:
            # Essayer de trouver un utilisateur avec l'adresse e-mail fournie
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            # Retourne None si l'utilisateur n'existe pas
            return None
        else:
            # Vérifier si le mot de passe est correct
            if user.check_password(password):
                return user
        return None
