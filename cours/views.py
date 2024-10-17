from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Cours, Message, Notification
from .serializers import CoursSerializer, MessageSerializer, NotificationSerializer

#Ajout d'un cours
class CoursCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        cours_serializer = CoursSerializer(data=request.data)
        if cours_serializer.is_valid():
            cours_serializer.save()
            return Response(cours_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(cours_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Suppression d'un cours
class CoursDeleteView(generics.DestroyAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        cours = self.get_object()
        if cours.teacher != request.user:
            raise PermissionDenied("Vous n'êtes pas l'enseignant de ce cours.")
        return super().delete(request, *args, **kwargs)

# Récupération les messages d'un cours spécifique
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        cours_id = self.kwargs['cours_id']
        return Message.objects.filter(cours_id=cours_id).order_by('timestamp')

# Envoie d'un message
class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cours_id = self.kwargs['cours_id']
        serializer.save(sender=self.request.user, cours_id=cours_id)

#récupération des notifications
class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)
