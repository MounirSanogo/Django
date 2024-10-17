from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError
from cours.models import Cours
from .models import Profile
from .serializers import EtudiantinscripSerializer, ProfileSerializer
from cours.serializers import CoursSerializer
from .utils import send_welcome_email
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import ProfileForm


#vues pour l'inscription
class EtudiantinscripView(APIView):
    def post(self, request):
        serializer = EtudiantinscripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_welcome_email(etudiant)
            return Response({"message": "Inscription réussie !"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#vues pour la connexion
class ConnexionetudiantView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # Authentifier l'utilisateur
        user = authenticate(request, username=email, password=password)

        if etudiant is not None:
            # Connexion réussie, générer un token ou retourner une réponse positive
            token, _ = Token.objects.get_or_create(etudiant=etudiant)  # Génère un token si nécessaire
            return Response({"token": token.key, "message": "Connexion réussie"}, status=status.HTTP_200_OK)
        else:
            # Connexion échouée, retourne une erreur
            return Response({"error": "Email ou mot de passe incorrect"}, status=status.HTTP_400_BAD_REQUEST)

#la liste des cours 
class CoursListView(generics.ListAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursSerializer


#vues pour le profil
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.etudiant_profile
