from app.models import Etablissement
from django.contrib import admin
from .models import Etablissement,Employer,Formation,Article
from django.utils.translation import ugettext_lazy
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User,Group
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
    search_fields=['region','adresse']

class FormationAdmin(admin.ModelAdmin):
    list_display=('nom_formation','niveau_requis')
    search_fields=['nom_formation']

admin_site.register(Etablissement,EtablissementAdmin)
admin_site.register(Employer)
admin_site.register(Formation,FormationAdmin)
admin_site.register(Article)
admin_site.register(User)
admin_site.register(Group)
