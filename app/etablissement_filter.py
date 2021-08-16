import django_filters
from .models import Etablissement,Formation,Employer
class EtablissemntsFilter(django_filters.FilterSet):
    # statut_proj= django_filters.CharFilter(field_name='ong__statut_proj', lookup_expr='iexact')
    #sect_iintervention=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Etablissement
        fields = ['region','departement','commune']


class FormationFilter(django_filters.FilterSet):
    region= django_filters.CharFilter(field_name='etablissement__region', lookup_expr='iexact')
    departement= django_filters.CharFilter(field_name='etablissement__departement', lookup_expr='iexact')
    etablissement= django_filters.NumberFilter(field_name='etablissement__id', lookup_expr='iexact')
    #sect_iintervention=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Formation
        fields = '__all__'