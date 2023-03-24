from datetime import date
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from PortfolioApp.models import *
from django.shortcuts import render
from django.http import HttpResponse
from PortfolioApp.serializers import *
from .models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import User, EducationCareer, Fonction, AwardAndHonors, AssociativeExperience, Biography, PhilosophicalStatement
from PIL import Image
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
import requests
# Create your views here.
import PortfolioBuilderApp
@api_view(['GET'])
def User_list_or_add(request):
    if request.method=='GET':
        user=User.objects.all() #get all  students from the database
        if  not user: #or if len(students) ==0 or if bool(students): #if there is no student in the list 
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer=UserSerializer(user,many=True) #convert student objects to json
        return Response(serializer.data,status=status.HTTP_200_OK)
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_user(request):
    if request.method=='POST':
        user=UserSerializer(data=request.data) #get the student object from the request after deserialization
        if user.is_valid(): #check if the student object is valid (all required fields are filled and fields data types and format are correct)
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message":"The method is not allowed"},status=status.HTTP_405_METHOD_NOT_ALLOWED)
     
@api_view(['GET', 'PUT', 'DELETE'])
def User_details_or_update_or_delete(request,pk):
    user= User()
    try:
        user = User.objects.get(idPersonne=pk)
    except user.DoesNotExist:
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #or more simply
    user=get_object_or_404(User, idPersonne=pk)
    if request.method=='GET':
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = UserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        user.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #or
    #return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 

@api_view(['GET', 'POST'])
def EducationCareer_list_or_add(request):
    if request.method=='GET':
        EducationCareer = EducationCareer.objects.all()
        if(len(EducationCareer)==0):
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = EducationCareerSerializer(EducationCareer, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = EducationCareerSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        #or
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def EducationCareer_details_or_update_or_delete(request, pk):
    try:
        educationCareer = EducationCareer.objects.get(id=pk)
    except educationCareer.DoesNotExist:
        return JsonResponse({'message': 'The Education Career does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #or more simply
    educationCareer=get_object_or_404(EducationCareer, id=pk)
    if request.method=='GET':
        serializer = EducationCareerSerializer(EducationCareer, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = EducationCareerSerializer(EducationCareer, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        educationCareer.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #or
    #return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 

@api_view(['GET', 'POST'])
def Fonction_list_or_add(request):
    if request.method=='GET':
        fonction = Fonction.objects.all()
        if(len(fonction)==0):
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = FonctionSerializer(Fonction, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = FonctionSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        #or
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def Fonction_details_or_update_or_delete(request, pk):
    try:
        fonction = Fonction.objects.get(id=pk)
    except fonction.DoesNotExist:
        return JsonResponse({'message': 'The Function does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #or more simply
    fonction=get_object_or_404(Fonction, id=pk)
    if request.method=='GET':
        serializer = FonctionSerializer(Fonction, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = FonctionSerializer(Fonction, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        fonction.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #or
    #return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 

@api_view(['GET', 'POST'])
def AwardAndHonors_list_or_add(request):
    if request.method=='GET':
        AwardandHonors = AwardAndHonors.objects.all()
        if(len(AwardandHonors)==0):
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = AwardAndHonorsSerializer(AwardAndHonors, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = AwardAndHonorsSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        #or
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def AwardAndHonors_details_or_update_or_delete(request, pk):
    try:
        AwardandHonors = AwardAndHonors.objects.get(id=pk)
    except AwardandHonors.DoesNotExist:
        return JsonResponse({'message': 'The Award and Honors does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #or more simply
    AwardandHonors=get_object_or_404(AwardAndHonors, id=pk)
    if request.method=='GET':
        serializer = AwardAndHonorsSerializer(AwardAndHonors, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = AwardAndHonorsSerializer(AwardAndHonors, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        AwardandHonors.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #or
    #return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
@api_view(['GET', 'POST'])
def AssociativeExperience_list_or_add(request):
    if request.method=='GET':
        Associativeexperience = AssociativeExperience.objects.all()
        if(len(Associativeexperience)==0):
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = AssociativeExperienceSerializer(AssociativeExperience, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = AssociativeExperienceSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        #or
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def AssociativeExperience_details_or_update_or_delete(request, pk):
    try:
        Associativeexperience = AssociativeExperience.objects.get(id=pk)
    except Associativeexperience.DoesNotExist:
        return JsonResponse({'message': 'The AAssociative experiences does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #or more simply
    Associativeexperience=get_object_or_404(AssociativeExperience, id=pk)
    if request.method=='GET':
        serializer = AssociativeExperienceSerializer(AssociativeExperience, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = AssociativeExperienceSerializer(AssociativeExperience, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        Associativeexperience.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #or
    #return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 

@api_view(['GET', 'POST'])
def Biography_list_or_add(request):
    if request.method=='GET':
        biography= Biography.objects.all()
        if(len(biography)==0):
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = BiographySerializer(Biography, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = BiographySerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        #or
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def Biography_details_or_update_or_delete(request, pk):
    try:
        biography = Biography.objects.get(id=pk)
    except biography.DoesNotExist:
        return JsonResponse({'message': 'The Biography does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #or more simply
    biography=get_object_or_404(Biography, id=pk)
    if request.method=='GET':
        serializer = BiographySerializer(Biography, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = BiographySerializer(Biography, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        biography.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #or
    #return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 




@api_view(['GET', 'POST'])
def PhilosophicalStatement_list_or_add(request):
    if request.method=='GET':
        Philosophicalstatement= PhilosophicalStatement.objects.all()
        if(len(Philosophicalstatement)==0):
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PhilosophicalStatementSerializer(PhilosophicalStatement, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = PhilosophicalStatementSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        #or
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def PhilosophicalStatement_details_or_update_or_delete(request, pk):
    try:
       Philosophicalstatement = PhilosophicalStatement.objects.get(id=pk)
    except Philosophicalstatement.DoesNotExist:
        return JsonResponse({'message': 'The Biography does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #or more simply
    Philosophicalstatement=get_object_or_404(PhilosophicalStatement, id=pk)
    if request.method=='GET':
        serializer = PhilosophicalStatementSerializer(PhilosophicalStatement, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = PhilosophicalStatementSerializer(PhilosophicalStatement, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        Philosophicalstatement.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #or
    #return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 


@api_view(['GET', 'POST'])
def ProfessionalAccomplishements_list_or_add(request):
    if request.method=='GET':
        Professionalaccomplishements= ProfessionalAccomplishements.objects.all()
        if(len(Professionalaccomplishements)==0):
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ProfessionalAccomplishementsSerializer(ProfessionalAccomplishements, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = ProfessionalAccomplishementsSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        #or
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def ProfessionalAccomplishements_details_or_update_or_delete(request, pk):
    try:
       Professionalaccomplishements = ProfessionalAccomplishements.objects.get(id=pk)
    except Professionalaccomplishements.DoesNotExist:
        return JsonResponse({'message': 'The Professional Accomplishements does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #or more simply
    Professionalaccomplishements=get_object_or_404(ProfessionalAccomplishements, id=pk)
    if request.method=='GET':
        serializer = ProfessionalAccomplishementsSerializer(ProfessionalAccomplishements, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = ProfessionalAccomplishementsSerializer(ProfessionalAccomplishements, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        Professionalaccomplishements.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #or
    #return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 



@api_view(['GET', 'POST'])
def References_list_or_add(request):
    if request.method=='GET':
        references= References.objects.all()
        if(len(references)==0):
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ReferencesSerializer(References, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializer = ReferencesSerializer(data=request.data, context={'request': request})
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        #or
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
      
@api_view(['GET', 'PUT', 'DELETE'])
def References_details_or_update_or_delete(request, pk):
    try:
       references= References.objects.get(id=pk)
    except references.DoesNotExist:
        return JsonResponse({'message': 'References does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #or more simply
    references=get_object_or_404(References, id=pk)
    if request.method=='GET':
        serializer = ReferencesSerializer(References, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method=='PUT':
        serializer = ReferencesSerializer(References, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    elif request.method=='DELETE':
        references.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #or
    #return JsonResponse({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED) 
  
   
def index(request):
    # Generate counts of some of the main objects
    user= User.objects.all().last()
    template = loader.get_template('index.html')
    nomUser = user.name
    familyName = user.familyName
    # Available books (status = 'a')
    Description = user.Careersummary
    photo= user.Photo
    
    # The 'all()' is implied by default.
    context = {
        'idPersonne': user.idPersonne,
        'name': nomUser,
        'familyName': familyName,
        'Description': Description,
        'photo': photo,
    }
# Render the HTML template index.html with the data in the context variable
    return HttpResponse(template.render(context, request))

def html(request):
    # Generate counts of some of the main objects
    user= User.objects.all().last()
    template = loader.get_template('html.html')
    education= EducationCareer.objects.all().last()
    fonction=Fonction.objects.all().last()
    award=AwardAndHonors.objects.all().last()
    AssoExperience=AssociativeExperience.objects.all().last()
    bio=Biography.objects.all().last()
    philo=PhilosophicalStatement.objects.all().last()
    pro=ProfessionalAccomplishements.objects.all().last()
    ref=References.objects.all().last()
    # The 'all()' is implied by default.
    context = {
        'user': user,
        'education':education,
        'fonction':fonction,
        'award':award,
        'asso':AssoExperience,
        'bio':bio,
        'philo':philo,
        'pro':pro,
        'ref':ref,
        
    
    }
# Render the HTML template index.html with the data in the context variable
    return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('form.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
    name = request.POST['name']
    fName = request.POST['familyName']
    mail=request.POST['mail']
    Career =request.POST['CareerSammary']
    if request.method == 'POST' and request.FILES['photo']:
        upload = request.FILES['photo']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        #return render(request, 'index.html', {'file_url': file_url})
    user = User(name=name, familyName=fName, email=mail, Careersummary=Career, Photo=upload)
    user.save()
    
    
    return HttpResponseRedirect(reverse('PortfolioApp:index'))



def delete(request, id):
  user = User.objects.get(idPersonne=id)
  user.delete()
  return HttpResponseRedirect(reverse('PortfolioApp:index'))

def update(request, id):
    template = loader.get_template('update.html')
    user = User.objects.get(idPersonne=id)
    name = request.POST.get('name')
    fName = request.POST.get('familyName')
    mail=request.POST.get('mail')
    Career =request.POST.get('CareerSammary')
   
    #user = User(name=name, familyName=fName, email=mail, Careersummary=Career)
    #user.save()
    context = {
    'name': name,
     }
    
    #user.save()
    return HttpResponse(template.render(context, request))


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successful." )
			return redirect("PortfolioApp:login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="login.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			user = authenticate(username=email, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {email}.")
				return redirect("PortfolioApp:index.html")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="index.html", context={"login_form":form})
