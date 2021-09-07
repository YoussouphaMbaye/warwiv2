from django.shortcuts import render
from .models import Article, Etablissement,Formation,Employer, Formation_modulaire
from .etablissement_filter import EtablissemntsFilter,FormationFilter, FormationModulairFilter
import csv
from django.core.paginator import Paginator
# Create your views here.
articles_recents=Article.objects.all().order_by('created_at')[:6]
def cartographie(request):
    etablissemnts_dj=Etablissement.objects.all()
    def format_for_leaflet(les_etablissements):
        list=[]
        for e in les_etablissements:
            list.append({'id':e.id,'nom_etablissement':e.nom_etablissement,'longittude':e.longitude,'lattitude':e.latitude,'region':e.region})
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
            list.append({'id':e.id,'nom_etablissement':e.nom_etablissement,'longittude':e.longitude,'lattitude':e.latitude,'region':e.region})
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
    
    etablissemnts=etablissemnts_dj
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
    mtype=request.GET['type']
    formations=None
    formations_m=None
    if mtype=='initiale':
        formations=Formation.objects.order_by().values('nom_formation').distinct()
    else:
        formations_m=Formation_modulaire.objects.order_by().values('nom_formation').distinct()
    
    mesParams=None
    get_param=request.GET.copy()
    if request.method=='GET':
        print(request.GET.get('d_attestation',False))
        if(request.GET.get('d_attestation',False)):
            
            get_param['diplome']='Attestation'
        if(request.GET.get('d_cap',False)):
            get_param['diplome']='CAP'
        if(request.GET.get('d_master',False)):
            get_param['diplome']='master'
        if(request.GET.get('d_licence',False)):
            get_param['diplome']='licence'
        if(request.GET.get('d_doctorat',False)):
            get_param['diplome']='doctorat'
        if(request.GET.get('d_d_dts',False)):
            get_param['diplome']='dts'
        if(request.GET.get('d_bts',False)):
            get_param['diplome']='bts'
        if(request.GET.get('d_bt',False)):
            get_param['diplome']='bt'
        if(request.GET.get('d_cs',False)):
            get_param['diplome']='CPS'
        
        if mtype=='initiale':
            formations=FormationFilter(get_param,formations).qs.order_by('nom_formation')
        else:
            formations_m=FormationModulairFilter(get_param,formations_m).qs.order_by('nom_formation')
        
        mesParams=request.GET
        

        page_obj=None
        page_obj_m=None
        if formations:
            paginator = Paginator(formations, 20)
            page_number = request.GET.get('page',1)
            page_obj = paginator.get_page(page_number)
        if formations_m:
            paginator_m = Paginator(formations_m, 20)
            page_number_m = request.GET.get('page_m',1)
            page_obj_m = paginator_m.get_page(page_number_m)
    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'lesformations.html',{'formations': page_obj,'articles_recents':articles_recents,'mesParams':mesParams,'formations_m':page_obj_m })
#etablissement par formation
def nomFormationTout(request):
    nom_formation=request.GET['nom_formation']
    formations_m=None
    formations=None
    mtype=request.GET['type']
    print(mtype)
    if mtype=='modulaire':
        print('dddddddddddddd')
        formations_m=Formation_modulaire.objects.filter(nom_formation__icontains=nom_formation)
    else:
        print('jjjjjjjjjjjjjjjjjjjjjjj')
        formations=Formation.objects.filter(nom_formation__icontains=nom_formation)
    
    
    mesParams=None
    get_param=request.GET.copy()
    if request.method=='GET':
        print(request.GET.get('d_attestation',False))
        if(request.GET.get('d_attestation',False)):
            
            get_param['diplome']='Attestation'
        if(request.GET.get('d_cap',False)):
            get_param['diplome']='CAP'
        if(request.GET.get('d_master',False)):
            get_param['diplome']='master'
        if(request.GET.get('d_cs',False)):
            
            get_param['diplome']='CPS'
        
        if(mtype=='modulaire'):
            formations_m=FormationModulairFilter(get_param,formations_m).qs
        else:
            formations=FormationFilter(get_param,formations).qs
            
        
        mesParams=request.GET
        

    page_obj_m=None
    page_obj=None  
    if formations:
        paginator = Paginator(formations, 20)
        page_number = request.GET.get('page',1)
        page_obj = paginator.get_page(page_number)
    
    if formations_m:
        paginator_m = Paginator(formations_m, 20)
        page_number_m = request.GET.get('page_m',1)
        page_obj_m = paginator_m.get_page(page_number_m)
    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'etablissementFormation.html',{'formations': page_obj,'articles_recents':articles_recents,'mesParams':mesParams,'formations_m':page_obj_m })

#details formations
def detailFormation(request,id):
    formation=Formation.objects.get(pk=id)

    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'detailsFormation.html',{'formation':formation,'articles_recents':articles_recents,'modulaire':'initiale'})
#details formations_modulaire
def detailFormationM(request,id):
    formation=Formation_modulaire.objects.get(pk=id)

    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'detailsFormation.html',{'formation':formation,'articles_recents':articles_recents,'modulaire':'modulaire'})

#details formations
def detailEtablissement(request,id,modulaire):
    print('=========================')
    etablissement=Etablissement.objects.get(pk=id)
    from_map={'lat':etablissement.latitude,'long':etablissement.longitude,'reg':etablissement.region}

    print(etablissement)
    formations=None #FormationFilter({'etablissement':int(id)},Formation.objects.all()).qs
    
    formations_m=Formation_modulaire.objects.filter(etablissement__id=int(id))
    
    formations=Formation.objects.filter(etablissement__id=int(id))

    #print(formations)
    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'detailsEtablissements.html',{'etablissement':etablissement,'formations':formations,'formations_m':formations_m,'from_map':from_map,'articles_recents':articles_recents,})


#formation agricolt
def formationAgricolt(request):
    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'formationAgricolt.html',{'articles_recents':articles_recents,})
#contact
def contact(request):
    if request.method=="POST":
        nom=request.POST['nom']
        objet=request.POST['objet']
        message=request.POST['message']
        print(nom+'\n'+objet+'\n'+message)
    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'contact.html',{'articles_recents':articles_recents})
#Actualité
def actualite(request):
    articles=Article.objects.all()
    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'actualite.html',{'articles':articles,'articles_recents':articles_recents,})
#Détails actualité
def detailsActualite(request,id):
    article=Article.objects.get(pk=id)
   
    articles_recents=Article.objects.all().order_by('created_at')[:5]
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
    articles_recents=Article.objects.all().order_by('created_at')[:5]
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

