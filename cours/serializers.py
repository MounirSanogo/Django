from rest_framework import serializers
from .models import Cours, Message, Notification

class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cours
        fields = ['id', 'title', 'description', 'tuteur', 'pdf_file', 'created_at']
# Méthode pour obtenir le nom complet de l'enseignant
    def get_tuteur_name(self, obj):
        return f"{obj.tuteur.nom} {obj.tuteur.prenom}"
 
#serialiseurs pour la messagerie
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'cours', 'content', 'timestamp']

#serialiseurs pour les notifications
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'message', 'cours', 'is_read', 'timestamp']
