
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home,name='accueil'),
    path('formations', views.les_formations,name='formations'),
    path('formationAgricolt', views.formationAgricolt,name='formationAgricolt'),
    path('formationDiplome', views.formationDiplome,name='formationDiplome'),
    path('formation/<int:id>', views.detailFormation,name='detailsFormation'),
    path('etablissement/<int:id>', views.detailEtablissement,name='detailsEtablissement'),
    path('cartographie', views.cartographie,name='cartographie'),
    path('actualite', views.actualite,name='actualite'),
    path('detailsActualite/<int:id>', views.detailsActualite,name='detailsActualite'),

    path('export', views.export_csv,name='export'),


]
