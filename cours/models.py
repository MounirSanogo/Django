from django.db import models
from django.contrib.auth import get_user_model

# courses/models.py

class Cours(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tuteur = models.ForeignKey('tuteurs.Tuteurinscrip', on_delete=models.CASCADE, related_name='cours')  # l'enseignant responsable du cours
    pdf_file = models.FileField(upload_to='cours_pdfs/', blank=True, null=True)# les fichiers pdf du cours
    created_at = models.DateTimeField(auto_now_add=True)# date de dépôt du cours

    def __str__(self):
        return self.title


# model/chat

User = get_user_model()

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} in {self.cours.title} at {self.timestamp}"

#model/notification

User = get_user_model()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="course_notifications") #L'utilisateur qui reçoit la notification (enseignant ou étudiant).
    message = models.TextField() #Le contenu de la notification.
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, related_name="notifications", null=True, blank=True) #Un lien facultatif avec un cours, si la notification est liée à un cours particulier.
    is_read = models.BooleanField(default=False) #Indique si la notification a été lue.
    timestamp = models.DateTimeField(auto_now_add=True) #Enregistre l'heure et la date de la création de la notification.

    def __str__(self):
        return f"Notification for {self.recipient} - Read: {self.is_read} - Course: {self.cours}"
