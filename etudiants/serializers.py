from rest_framework import serializers
from .models import Etudiantinscrip, Profile
from django.contrib.auth import get_user_model

# sérialiseur du formulaire d'inscription
class EtudiantinscripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiantinscrip
        fields = ['id', 'nom', 'prenom', 'email', 'password', 'confirm_password']

        def validate(self, data):
            if data['password'] != data['confirm_password']:
                raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
            return data

        def create(self, validated_data):
            etudiant = etudiant.objects.create(
                nom=validated_data['nom'],
                prenom=validated_data['prenom'],
                email=validated_data['email']
            )
            etudiant.set_password(validated_data['password'])  # Hashage du mot de passe
            etudiant.save()
            return etudiant


# sérialiseur du profil des etudiants 

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']


