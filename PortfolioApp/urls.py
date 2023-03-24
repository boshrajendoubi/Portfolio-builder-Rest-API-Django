from django.urls import path,include
from rest_framework import routers
from . import views,viewsets
import PortfolioApp.urls
#urls using ModelViewSet
from PortfolioApp.viewsets import *


#add router for each viewset  to the router object
#each time we use the path '/User' in the url, 
#the UserViewSet will be called
#the prefix r is used to indicate that the string is a raw string (not interpret the backslash as an escape character)
router=routers.DefaultRouter()
router.register(r'Userview',UserViewSet)

router.register(r'EducationCareer',EducationCareerViewSet)
router.register(r'Fonction',FonctionViewSet)
router.register(r'AwardAndHonors',AwardAndHonorsViewSet)
router.register(r'AssociativeExperience',AssociativeExperienceViewSet)
router.register(r'Biography',BiographyViewSet)
router.register(r'PhilosophicalStatement',PhilosophicalStatementViewSet)
router.register(r'ProfessionalAccomplishements',ProfessionalAccomplishementsViewSet)
router.register(r'References',ReferencesViewSet)
#router.register(r'userviewset',UserViewSet)
# #add the router to the urlpatterns
# urlpatterns = [
#     path('', include(router.urls)),
# ]
app_name = 'PortfolioApp'
urlpatterns = [
    path('', include(router.urls)),
    path(r"User/all/",views.User_list_or_add),
    path(r'User/add/',views.add_user),
    path(r'EducationCareer/all/',views.EducationCareer_list_or_add),
    path(r'EducationCareer/add/',views.User_details_or_update_or_delete),
    path(r'Fonction/all/',views.Fonction_list_or_add),
    path(r'Fonction/add/',views.Fonction_details_or_update_or_delete),
    path(r'AwardAndHonors/all/',views.AwardAndHonors_list_or_add),
    path(r'AwardAndHonors/add/',views.AwardAndHonors_details_or_update_or_delete),  
    path(r'AssociativeExperience/all/',views.AssociativeExperience_list_or_add),
    path(r'AssociativeExperience/add/',views.AssociativeExperience_details_or_update_or_delete),
    path(r'Biography/all/',views.Biography_list_or_add),
    path(r'Biography/add/',views.Biography_details_or_update_or_delete),
    path(r'PhilosophicalStatement/all/',views.PhilosophicalStatement_list_or_add),
    path(r'PhilosophicalStatement/add/',views.PhilosophicalStatement_details_or_update_or_delete),
    path(r'ProfessionalAccomplishements/all/',views.ProfessionalAccomplishements_list_or_add),
    path(r'ProfessionalAccomplishements/add/',views.ProfessionalAccomplishements_details_or_update_or_delete),
    path(r'References/all/',views.References_list_or_add),
    path(r'References/add/',views.References_details_or_update_or_delete),
    path('index',views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("portfolioshow", views.html, name="html"),
    #path('accounts/', include('django_registration.backends.activation.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    
   
 
    ]


