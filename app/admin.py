from app.models import Etablissement
from django.contrib import admin
from .models import Demande, Etablissement,Employer,Formation,Article,Formation_modulaire
from django.utils.translation import ugettext_lazy
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User,Group
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Etablissement)
admin.site.register(Employer)
admin.site.register(Formation)
admin.site.register(Article)

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('My site admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('My administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Site administration')
admin_site = MyAdminSite()

class EtablissementAdmin(admin.ModelAdmin):
    list_display=('nom_etablissement','region','ia','ief','adresse')
    search_fields=['nom_etablissement','region','adresse']
    list_filter=('statut_juridique','partenaire_principal')

class FormationAdmin(admin.ModelAdmin):
    list_display=('nom_formation','etablissement')
    list_filter=('niveau_requis','c_concours','c_dossier','c_autre','c_entretien','d_dts','d_bts','d_bt','d_cs','d_bac','d_licence','d_master','d_doctorat','d_attestation','d_certificat',('etablissement',admin.RelatedOnlyFieldListFilter))
    search_fields=['nom_formation']

class FormationModulaireAdmin(admin.ModelAdmin):
    list_display=('nom_formation','etablissement')
    list_filter=('niveau_requis','c_concours','c_dossier','c_autre','c_entretien','diplome',('etablissement',admin.RelatedOnlyFieldListFilter))
    search_fields=['nom_formation',]
class DemandeAdmin(admin.ModelAdmin):
    list_display=('nom_etablissement','email','telephone','message')
    search_fields=['nom_etablissement']
admin_site.register(Etablissement,EtablissementAdmin)
admin_site.register(Employer)
admin_site.register(Formation,FormationAdmin)
admin_site.register(Formation_modulaire,FormationModulaireAdmin)
admin_site.register(Demande,DemandeAdmin)
admin_site.register(Article)
class UserAdmin(UserAdmin):
    #inlines = (UserInfoInline,)
    list_display = ('username', 'first_name', 'last_name')
admin_site.register(User,UserAdmin)
admin_site.register(Group)
