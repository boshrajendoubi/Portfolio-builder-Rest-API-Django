from rest_framework import serializers
from .models import *
class PersonneSerializer(serializers.ModelSerializer):
    class meta :
        model=Personne
        fields='__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__' #serializes all fields
class EducationCareerSerializer(serializers.ModelSerializer):
    class Meta:
        model=EducationCareer
        fields='__all__' #serializes all fields
class FonctionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Fonction
        fields='__all__' #serializes all fields
class AwardAndHonorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AwardAndHonors
        fields='__all__' #serializes all fields
class AssociativeExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=AssociativeExperience
        fields='__all__' #serializes all fields
class BiographySerializer(serializers.ModelSerializer):
    class Meta:
        model=Biography
        fields='__all__' #serializes all fields
class PhilosophicalStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model=PhilosophicalStatement
        fields='__all__' #serializes all fields
class ProfessionalAccomplishementsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfessionalAccomplishements
        fields='__all__' #serializes all fields
class ReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model=References
        fields='__all__' #serializes all fields