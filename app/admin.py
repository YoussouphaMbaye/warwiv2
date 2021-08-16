from app.models import Etablissement
from django.contrib import admin
from .models import Etablissement,Employer,Formation,Article
# Register your models here.
admin.site.register(Etablissement)
admin.site.register(Employer)
admin.site.register(Formation)
admin.site.register(Article)
