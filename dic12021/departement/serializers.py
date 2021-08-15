from .models import *
from users.models import *
from django.contrib.auth.models import User
from rest_framework import  serializers, viewsets
from django.contrib.auth import authenticate

class listeEtudiantsSerializers(serializers.ModelSerializer):
    prenom = serializers.ReadOnlyField(source='etudiant.user.first_name')
    nom = serializers.ReadOnlyField(source='etudiant.user.last_name')
    numero_carte = serializers.ReadOnlyField(source='etudiant.numero_carte')
    departement = serializers.ReadOnlyField(source='classe.dept.nom_dept')
    niveau = serializers.ReadOnlyField(source='classe.niveau.niveau')
    class Meta:
        model = Etudiant_Classe
        fields=['prenom', 'nom','numero_carte','departement','niveau','annee_scolaire']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")
