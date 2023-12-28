from django.forms import fields, models, widgets
from .models import Demande
from django import forms
from django.utils.translation import ugettext_lazy as _

class DemandeForms(forms.ModelForm):
    class Meta:
        model=Demande
        fields=('nom_etablissement','email','telephone','nom_ref','message')
        widgets={
            'nom_etablissement':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'telephone':forms.TextInput(attrs={'class':'form-control'}),
            'nom_ref':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control ','rows':'2'})

        }
        labels = {
            "nom_etablissement": _("Nom établissement"),
            "telephone": _("Téléphone"),
            "nom_ref":_("Nom du référent")
        }