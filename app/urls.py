
from django.urls import path
from . import views 
from .admin import admin_site
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns = [
    path('', views.home,name='accueil'),
    path('formations', views.les_formations,name='formations'),
    #path('etablissementFormation', views.les_,name='formations'),
    path('formationAgricolt', views.formationAgricolt,name='formationAgricolt'),
    path('formationDiplome', views.formationDiplome,name='formationDiplome'),
    
    path('nomFormationTout', views.nomFormationTout,name='nomFormationTout'),
    path('formation/<int:id>', views.detailFormation,name='detailsFormation'),
    path('formationM/<int:id>', views.detailFormationM,name='detailsFormationM'),
    path('etablissement/<int:id>', views.detailEtablissement,name='detailsEtablissement'),
    path('cartographie', views.cartographie,name='cartographie'),
    path('actualite', views.actualite,name='actualite'),
    path('contact', views.contact,name='contact'),
    path('send_email', views.send_email,name='send_email'),
    path('aPropos', views.a_propos,name='apropos'),
    path('demande', views.demande,name='demader'),
    path('detailsActualite/<int:id>', views.detailsActualite,name='detailsActualite'),

    path('export', views.export_csv,name='export'),
    path('plaquette',views.plaquettePDF,name='plaquettePDF'),
    #path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico')))


]
handler404 = 'app.views.error_404'
handler500 = 'app.views.error_500'
