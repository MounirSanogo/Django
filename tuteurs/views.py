from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAuthenticated
from .serializers import TuteurinscripSerializer, ProfileSerializer
from .utils import send_welcome_email
from django.contrib.auth import authenticate
from cours.models import Cours
from .models import Profile
from cours.serializers import CoursSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm

#inscription d'un tuteur
class TuteurinscripView(APIView):
    def post(self, request):
        serializer = TuteurinscripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_welcome_email(tuteur)
            return Response({"message": "Inscription réussie !"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#connexion d'un tuteur
class ConnexiontuteurView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authentifier l'utilisateur
        user = authenticate(request, username=email, password=password)

        if tuteur is not None:
            # Connexion réussie, générer un token ou retourner une réponse positive
            token, _ = Token.objects.get_or_create(tuteur=tuteur)  # Génère un token si nécessaire
            return Response({"token": token.key, "message": "Connexion réussie"}, status=status.HTTP_200_OK)
        else:
            # Connexion échouée, retourne une erreur
            return Response({"error": "Email ou mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)

# lister et créer des cours
class TeacherCourseListCreateView(generics.ListCreateAPIView):
    serializer_class = CoursSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Récupère uniquement les cours créés par l'enseignant connecté
        return Cours.objects.filter(tuteur=self.request.user)

    def perform_create(self, serializer):
        # Lors de la création d'un cours, l'enseignant connecté est automatiquement associé
        serializer.save(teacher=self.request.user)


#vues pour le profil 
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.teacher_profile
