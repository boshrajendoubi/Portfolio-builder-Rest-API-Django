from .serializers import *
from rest_framework import viewsets
from .models import *
from rest_framework.response import Response
"""class PersonneViewSet(viewsets.ModelViewSet):

    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']"""
    
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class USer1ViewSet(viewsets.ViewSet):
    #.....
    def partial_update(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            #.... Your code ....
            serializer.save()
            return Response(serializer.data)

class EducationCareerViewSet(viewsets.ModelViewSet):

    queryset = EducationCareer.objects.all()
    serializer_class = EducationCareerSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class FonctionViewSet(viewsets.ModelViewSet):

    queryset = Fonction.objects.all()
    serializer_class =FonctionSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class AwardAndHonorsViewSet(viewsets.ModelViewSet):

    queryset = AwardAndHonors.objects.all()
    serializer_class =AwardAndHonorsSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class AssociativeExperienceViewSet(viewsets.ModelViewSet):

    queryset = AssociativeExperience.objects.all()
    serializer_class =AssociativeExperienceSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']
class BiographyViewSet(viewsets.ModelViewSet):

    queryset = Biography.objects.all()
    serializer_class =BiographySerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']
class PhilosophicalStatementViewSet(viewsets.ModelViewSet):

    queryset = PhilosophicalStatement.objects.all()
    serializer_class =PhilosophicalStatementSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class ProfessionalAccomplishementsViewSet(viewsets.ModelViewSet):

    queryset = ProfessionalAccomplishements.objects.all()
    serializer_class =ProfessionalAccomplishementsSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']

class ReferencesViewSet(viewsets.ModelViewSet):
    queryset = References.objects.all()
    serializer_class =ReferencesSerializer
    http_method_name = ['get', 'post', 'put', 'delete','patch']
    
