from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(tuteur):
    subject = 'Bienvenue sur notre plateforme'
    message = f'Bonjour {tuteur.nom},\n\nMerci de vous être inscrit sur notre plateforme ! Nous sommes ravis de vous accueillir.'
    
    recipient_list = [tuteur.email]
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=False)