from rest_framework import serializers
from .models import Tuteurinscrip, Profile
from django.contrib.auth import get_user_model

# sérialiseur d'inscription
class TuteurinscripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuteurinscrip
        fields = ['id', 'nom', 'prenom', 'email', 'password', 'confirmpassword']

        def validate(self, data):
            if data['password'] != data['confirmpassword']:
                raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
            return data

        def create(self, validated_data):
            tuteur = Tuteur.objects.create(
                nom=validated_data['nom'],
                prenom=validated_data['prenom'],
                email=validated_data['email']
            )
            tuteur.set_password(validated_data['password'])  # Hashage du mot de passe
            tuteur.save()
            return tuteur

# sérialiseur du profil 
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']

