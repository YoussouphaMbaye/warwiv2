from django.shortcuts import render
from .models import Article, Etablissement,Formation,Employer
from .etablissement_filter import EtablissemntsFilter,FormationFilter
import csv
from django.core.paginator import Paginator
# Create your views here.
articles_recents=Article.objects.all().order_by('created_at')[:6]
def cartographie(request):
    etablissemnts_dj=Etablissement.objects.all()
    def format_for_leaflet(les_etablissements):
        list=[]
        for e in les_etablissements:
            list.append({'id':e.id,'nom_etablissement':e.nom_etablissement,'longittude':e.longittude,'lattitude':e.lattitude,'region':e.region})
        return list
    
    def getRegions(les_etablissements):
        lisReg=[]
        listDep=[]
        lisCommune=[]
        for e in les_etablissements:
            lisReg.append(e.region)
            lisCommune.append(e.commune)
            listDep.append(e.departement)

        return set(lisReg) ,set(lisCommune),set(listDep)
        req_departement=""
    req_commune=""
    req_departement=""
    req_region=""
    etablissemnts=format_for_leaflet(etablissemnts_dj)
    if request.method=="POST":
        req_departement=request.POST['departement']
        req_commune=request.POST['commune']
        req_region=request.POST['region']
        etablissemnts_dj=EtablissemntsFilter(request.POST,etablissemnts_dj).qs
        etablissemnts=format_for_leaflet(etablissemnts_dj)
    regions,communes,departements=getRegions(etablissemnts_dj)
    return render(request,'cartographie.html',{'etablissements':etablissemnts,'regions':regions,'communes':communes,
    'departements':departements,
    'req_departement':req_departement,
    'req_commune':req_commune,
    'req_region':req_region,
    'articles_recents':articles_recents,
    })

def home(request):
    formations=Formation.objects.all()
    etablissemnts_dj=Etablissement.objects.all()
    nb_etablissement=len(etablissemnts_dj)
    nb_fromation=len(formations)
    print("-----------------------hhhhhhhhhhhh----------------------")
    def format_for_leaflet(les_etablissements):
        list=[]
        for e in les_etablissements:
            list.append({'id':e.id,'nom_etablissement':e.nom_etablissement,'longittude':e.longittude,'lattitude':e.lattitude,'region':e.region})
        return list

    def getRegions(les_etablissements):
        lisReg=[]
        listDep=[]
        lisCommune=[]
        for e in les_etablissements:
            lisReg.append(e.region)
            lisCommune.append(e.commune)
            listDep.append(e.departement)

        return set(lisReg) ,set(lisCommune),set(listDep)
    
    etablissemnts=format_for_leaflet(etablissemnts_dj)
    req_departement=""
    req_commune=""
    req_region=""
    if request.method=="POST":
        req_departement=request.POST['departement']
        req_commune=request.POST['commune']
        req_region=request.POST['region']
        
        etablissemnts_dj=EtablissemntsFilter(request.POST,etablissemnts_dj).qs
    regions,communes,departements=getRegions(etablissemnts_dj)
    #article recents
    articles_recents=Article.objects.all().order_by('created_at')[:5]

    return render(request, 'index.html',{'etablissements':etablissemnts,'regions':regions,'communes':communes,
    'departements':departements,
    'req_departement':req_departement,
    'req_commune':req_commune,
    'req_region':req_region,
    'formations':formations,
    'nb_etablissement':nb_etablissement,
    'nb_formation':nb_fromation,
    'articles_recents':articles_recents})



#formation
def les_formations(request):
    formations=Formation.objects.all()
    mesParams=None
    if request.method=='GET':
        formations=FormationFilter(request.GET,formations).qs
        
        mesParams=request.GET
        

        
    
    paginator = Paginator(formations, 16)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    return render(request,'lesformations.html',{'formations': page_obj,'articles_recents':articles_recents,'mesParams':mesParams})

#details formations
def detailFormation(request,id):
    formation=Formation.objects.get(pk=id)
    
    return render(request,'detailsFormation.html',{'formation':formation,'articles_recents':articles_recents,})

#details formations
def detailEtablissement(request,id):
    print('=========================')
    etablissement=Etablissement.objects.get(pk=id)
    from_map={'lat':etablissement.lattitude,'long':etablissement.longittude,'reg':etablissement.region}
    
    print(etablissement)
    formations=None #FormationFilter({'etablissement':int(id)},Formation.objects.all()).qs
    formations=Formation.objects.filter(etablissement_id=id)
    print(formations)
    return render(request,'detailsEtablissements.html',{'etablissement':etablissement,'formations':formations,'from_map':from_map,'articles_recents':articles_recents})


#formation agricolt
def formationAgricolt(request):
    return render(request,'formationAgricolt.html',{'articles_recents':articles_recents,})
#Actualité
def actualite(request):
    articles=Article.objects.all()
    return render(request,'actualite.html',{'articles':articles,'articles_recents':articles_recents,})
#Détails actualité
def detailsActualite(request,id):
    article=Article.objects.get(pk=id)
   
    print(articles_recents)
    return render(request,'actualiteDetails.html',{'article':article,'articles_recents':articles_recents})


#formation diplome
def formationDiplome(request):
    etablissemnts_dj=Etablissement.objects.all()
    def getRegions(les_etablissements):
        lisReg=[]
        listDep=[]
        lisCommune=[]
        for e in les_etablissements:
            lisReg.append(e.region)
            lisCommune.append(e.commune)
            listDep.append(e.departement)

        return set(lisReg) ,set(lisCommune),set(listDep)

    req_departement=""
    req_commune=""
    req_region=""
    if request.method=="POST":
        req_departement=request.POST['departement']
        req_commune=request.POST['commune']
        req_region=request.POST['region']
        etablissemnts_dj=EtablissemntsFilter(request.POST,etablissemnts_dj).qs
    regions,communes,departements=getRegions(etablissemnts_dj)
    
    return render(request,'formationsDiplome.html',{'etablissements':etablissemnts_dj,'regions':regions,'communes':communes,
    'departements':departements,
    'req_departement':req_departement,
    'req_commune':req_commune,
    'req_region':req_region,
    'articles_recents':articles_recents,
    })
def export_csv(request):
    with open('your.csv', 'wb') as csvfile:
        a=''
        for field in Formation._meta.fields:
            a+=field.name+';'
            print(a)
        writer = csv.writer(csvfile)
        # write your header first
        for obj in Formation.objects.all():
            row = ""
            for field in Formation._meta.fields:
                row += getattr(obj, field.name) + ","
            writer.writerow(row)

