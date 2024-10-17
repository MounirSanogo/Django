from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User
from django.contrib.auth import get_user_model
from cours.models import Cours
from django.conf import settings


#inscription des etudiants
class Etudiantinscrip(models.Model):
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=10)
    confirm_password = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.Nom} {self.Prenom}'  

#profil des etudiants
User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='etudiant_profile')
    bio = models.TextField(blank=True, null=True)  # Exemple de champ supplémentaire
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Profile de {self.user.username}"

