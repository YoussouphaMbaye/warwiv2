
from django.urls import path
from . import views 
from .admin import admin_site


urlpatterns = [
    path('', views.home,name='accueil'),
    path('formations', views.les_formations,name='formations'),
    #path('etablissementFormation', views.les_,name='formations'),
    path('formationAgricolt', views.formationAgricolt,name='formationAgricolt'),
    path('formationDiplome', views.formationDiplome,name='formationDiplome'),
    
    path('nomFormationTout', views.nomFormationTout,name='nomFormationTout'),
    path('formation/<int:id>', views.detailFormation,name='detailsFormation'),
    path('formationM/<int:id>', views.detailFormationM,name='detailsFormationM'),
    path('etablissement/<int:id>/<str:modulaire>', views.detailEtablissement,name='detailsEtablissement'),
    path('cartographie', views.cartographie,name='cartographie'),
    path('actualite', views.actualite,name='actualite'),
    path('contact', views.contact,name='contact'),
    path('detailsActualite/<int:id>', views.detailsActualite,name='detailsActualite'),

    path('export', views.export_csv,name='export'),


]
