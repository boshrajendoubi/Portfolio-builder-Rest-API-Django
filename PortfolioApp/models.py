from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

CategorieCareer=[
    ('Bac', 'Baccaleaureat'),
    ('Licence1', 'L1'),
    ('Licence2', 'L2'),
    ('Licence3', 'L3'),
    ('Master1', 'M1'),
    ('Master2', 'M2'),
    ('PHD', 'Phd'),
    ('Engineering1', 'Engineering 1'),
    ('Engineering2', 'Engineering 2')
]
LevelR=[
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low')
]
softSkills=[
     ('communication', 'communication'),
     ('Team work', 'Team work'),
     ('stress management', 'stress management'),
     ('solution oriented', 'solution oriented'),
     ('orthers', 'others')
     
]

sociallink=[
    ('facebook' , 'Facebook'),
    ('Linkedin', 'Linkedin'),
    ('Other','Other')
]

CategoriePro=[
    ('Work' , 'Work'),
    ('PersonalProject' , 'PersonalProject'),
    ('freelance' , 'freelance'),
    ('internship' , 'internship')   
]



class Personne(models.Model): 
    idPersonne=models.AutoField(primary_key=True)
    name = models.CharField(max_length = 100,verbose_name='name: ', null = False , blank = False, editable=True)
    familyName = models.CharField(max_length = 100, null = False , blank = False, verbose_name='family name: ',editable=True)
    Photo=models.ImageField(default='311872633_630546525429055_6007909932726738695_n.jpg',upload_to = "photos/", max_length = 200, editable=True)
        
    def __str__(self):
        return "name = %s, family name = %s " %(self.name, self.familyName)
    class Meta: 
        abstract = True 
        ordering = ['name', 'familyName']
         

        
class User(Personne):
    email = models.EmailField(verbose_name = "email ", max_length=60)
    password=models.CharField(max_length = 100,verbose_name='Password:  ', null = False , blank = False)
    Careersummary = models.CharField(max_length = 500,verbose_name='Decribe yourself ', null = False , blank = False)
    def __str__(self):
        return 'email = %s, \n password = %s' %(self.email, self.password)
 
    class Meta:
        db_table = 'User'
    
    
     
        

    
        
class EducationCareer(models.Model):
    educationCareer = models.ForeignKey(User , on_delete=models.CASCADE)
    level = models.CharField(max_length = 12, choices = CategorieCareer, default = CategorieCareer[0][0])
    description = models.CharField(max_length = 500,verbose_name='Decribe yourself ', null = False , blank = False)
    year=models.DateField(default = date.today().year)
    place=models.CharField(max_length = 100,verbose_name='place: ', null = False , blank = False)
    justification=models.FileField(upload_to='Career/files', max_length=254)
    def __str__(self):
        return 'education_career = %s, \n level = %s, \n description = %s , \n year =%s , \n place=%s , \n justification =%s' %(self.educationCareer, self.level, self.description , self.year , self.place , self.justification)

    class Meta:
        db_table = 'EducationCareer'
    
    
class Fonction(models.Model):
    fonction = models.ForeignKey(User , on_delete=models.CASCADE)
    titlePost = models.CharField(max_length = 100,verbose_name='Job title:  ', null = False , blank = False)
    dateFonction=models.DateField(default = date.today)
    place=models.CharField(max_length = 100,verbose_name='place: ', null = False , blank = False)
    def __str__(self):
        return 'fonction = %s, \n Title_post = %s, \n Date_fonction = %s, \n place = %s' %(self.fonction, self.titlePost, self.dateFonction , self.place)

    class Meta:
        db_table = 'Fonction'
    

class AwardAndHonors(models.Model):
    awardAndHonors = models.ForeignKey(User , on_delete=models.CASCADE)
    awardNAme = models.CharField(max_length = 100,verbose_name='award title:  ', null = False , blank = False)
    obtentionDate = models.DateField(default = date.today)
    levelR = models.CharField(max_length = 10, choices = LevelR, default = LevelR[0][0])
    justification=models.FileField(upload_to='honors/files', max_length=254)
    def __str__(self):
        return 'Awards_and_honors = %s, \n Award_name = %s, \n obtention_date=%s , \n Level_recognation = %s , \n justification =%s' %(self.awardAndHonors, self.awardNAme, self.obtentionDate , self.levelR, self.justification)

    class Meta:
        db_table = 'AwardAndHonors'

class AssociativeExperience(models.Model):
     associativeExperience = models.ForeignKey(User , on_delete=models.CASCADE)
     post = models.CharField(max_length = 100,verbose_name='Position:  ', null = False , blank = False)
     emplacement=models.CharField(max_length = 100,verbose_name='Position:  ', null = False , blank = False)
     dateDebut=models.DateField(default = date.today)
     dateFin=models.DateField(default = date.today)
     description = models.CharField(max_length = 500,verbose_name='Decribe yourself ', null = False , blank = False)
     def __str__(self):
        return 'Associative_Experience = %s, \n post = %s, \n emplacement = %s , \n date_debut= %s , \n date_fin= %s , \n description = %s' %(self.associativeExperience, self.post, self.emplacement,self.dateDebut,self.dateFin,self.description)

     class Meta:
        db_table = 'AssociativeExperience'

class Biography(models.Model):
    biography = models.ForeignKey(User , on_delete=models.CASCADE)
    softskills=models.CharField(max_length = 17, choices = softSkills, default = softSkills[0][0])
    email = models.EmailField(verbose_name = "email ", max_length=60)
    SocialLinkType=models.CharField(max_length = 10, choices = sociallink, default = sociallink[0][0])
    SocialLink= models.URLField(verbose_name = "url:  ", max_length=300)
    PhoneNumber=models.PositiveBigIntegerField(verbose_name = "phone number:   ")
    personalWebSite= models.URLField(verbose_name = "Personal website  ", max_length=300)
    def __str__(self):
        return 'biography = %s, \n soft_skills = %s, \n email = %s , \n social_link_type=%s , \n Social_link=%s , \n Phone_number =%s , \n personal_website =%s' %(self.biography, self.softskills, self.email,self.SocialLinkType, self.SocialLink, self.PhoneNumber, self.personalWebSite)

    class Meta:
        db_table = 'Biography'

    
    
class PhilosophicalStatement(models.Model):
    philosophicalStatement = models.ForeignKey(User , on_delete=models.CASCADE)
    missionStatement=models.CharField(max_length = 100,verbose_name='Mission Emplacement:  ', null = False , blank = False)
    board = ArrayField(
        ArrayField(
            models.CharField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )
    def __str__(self):
        return 'philosophical_statement = %s, \n mission_statement = %s, \n board = %s' %(self.philosophicalStatement, self.missionStatement, self.board)

    class Meta:
        db_table = 'PhilosophicalStatement'

    
    
class ProfessionalAccomplishements(models.Model):
    professionalAccomplishements = models.ForeignKey(User , on_delete=models.CASCADE)
    CategorieProfessional = models.CharField(max_length = 15, choices = CategoriePro, default = CategoriePro[0][0])
    titlework = models.CharField(max_length = 100,verbose_name='title:  ', null = False , blank = False)
    justification=models.FileField(upload_to='Accomplishment/files', max_length=254)
    def __str__(self):
        return 'Professional_accomplisment = %s, \n Professional_categorie = %s, \n Title_work = %s , \n jsutification = %s' %(self.professionalAccomplishements, self.CategorieProfessional, self.titlework , self.justification)

    class Meta:
        db_table = 'ProfessionalAccomplishements'

class References(Personne):
    email = models.EmailField(verbose_name = "email ", max_length=60)
    PhoneNumber=models.PositiveBigIntegerField(verbose_name = "phone number:   ")
    def __str__(self):
        return 'References = %s,\n email = %s, \n PhoneNumber = %s' %(self.references, self.email, self.PhoneNumber)

    class Meta:
        db_table = 'References'


        
     


     
     
     
    
       
    

# Create your models here.
