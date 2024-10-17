from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .utils import send_welcome_email
from .models import Profile
from django.contrib.auth.models import User

User = get_user_model()

@receiver(post_save, sender=User)

def send_welcome_email_signal(sender, instance, created, **kwargs):
    if created:  # Vérifie si l'utilisateur vient d'être créé
        send_welcome_email(instance)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Créer automatiquement un profil lorsqu'un utilisateur est créé
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Sauvegarder le profil lorsqu'un utilisateur est sauvegardé
    instance.profile.save()
