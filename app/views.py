from django.shortcuts import redirect, render

from app.forms import DemandeForms
from .models import Article, Etablissement,Formation,Employer, Formation_modulaire
from .etablissement_filter import EtablissemntsFilter,FormationFilter, FormationModulairFilter
import csv
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from django.core.mail import send_mail

from django.http import HttpResponseRedirect, Http404, FileResponse

from django.urls import reverse
def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def error_500(request):
        data = {}
        return render(request,'404.html', data)
def plaquettePDF(request):
        
        return FileResponse(open("static/assets/PlaquetteFAR.pdf", 'rb'), content_type='application/pdf')
#send_email
def send_email(request):
    articles_recents=Article.objects.all().order_by('created_at')[:5]
    if request.method=="POST":
        e_email=request.POST['email_email']
        e_nom=request.POST['email_nom']
        e_message=request.POST['email_message']
        e_objet =request.POST['email_objet']
        #send_mail(e_nom+": "+e_objet,e_message,e_email,['contact@warwi.org'])
        return render(request,'contact.html',{'articles_recents':articles_recents,'message':True,'e_nom':e_nom})

    return render(request,'contact.html',{'articles_recents':articles_recents,'message':False})
# Create your views here.
articles_recents=Article.objects.all().order_by('created_at')[:6]
def cartographie(request):
    #etablissemnts_dj=Etablissement.objects.all()
    formations=Formation.objects.all().distinct('etablissement__id')
    form_uni=Formation.objects.all().distinct('nom_formation')
    form_uni_m=Formation_modulaire.objects.all().distinct('nom_formation')
    # lesFormationsNon=[]
    # for f in form_uni:
    #     lesFormationsNon.append(f.nom_formation)
    # for f in form_uni_m:
    #     lesFormationsNon.append(f.nom_formation)
    # lesFormationsNon=set(lesFormationsNon)
    eta=[]
    for f in formations:
        eta.append(f.etablissement.id)
        print(f.etablissement.id)
    print('--------------')
    fm=Formation_modulaire.objects.all().exclude(etablissement__id__in=eta).distinct('etablissement__id')
    eta=[]
    for f_m in fm:
        print(f_m.id)
    #formations_m=Formation_modulaire.objects.all()
    def format_for_leaflet_b(les_formations,les_formations_m):
        list=[]
        for f in les_formations:
            list.append({'id':f.etablissement.id,'nom_etablissement':f.etablissement.nom_etablissement,'longittude':f.etablissement.longitude,'lattitude':f.etablissement.latitude,'region':f.etablissement.region,'statut_juridique':f.etablissement.statut_juridique})
        if les_formations_m:
            for f in les_formations_m:
                list.append({'id':f.etablissement.id,'nom_etablissement':f.etablissement.nom_etablissement,'longittude':f.etablissement.longitude,'lattitude':f.etablissement.latitude,'region':f.etablissement.region,'statut_juridique':f.etablissement.statut_juridique})
        
        return list
    
    def format_for_leaflet(les_formations):
        list=[]
        for f in les_formations:
            list.append({'id':f.etablissement.id,'nom_etablissement':f.etablissement.nom_etablissement,'longittude':f.etablissement.longitude,'lattitude':f.etablissement.latitude,'region':f.etablissement.region,'statut_juridique':f.etablissement.statut_juridique})
        return list
    def getFormation(lesFormation):
        list_nom_form=[]
        for f in lesFormation:
            list_nom_form.append(f.nom_formation)
        return list_nom_form

    def getRegions(formations,formations_m):
        lisReg=[]
        listDep=[]
        lisCommune=[]
        statut_j=[]
        nom_etablissements=[]
        lesFormationsNon=[]
        for e in formations:
            lisReg.append(e.etablissement.region)
            lisCommune.append(e.etablissement.commune)
            listDep.append(e.etablissement.departement)
            statut_j.append(e.etablissement.statut_juridique)
            nom_etablissements.append(e.etablissement.nom_etablissement)
            lesFormationsNon.append(e.nom_formation)
        if formations_m:
            for e in formations_m:
                lisReg.append(e.etablissement.region)
                lisCommune.append(e.etablissement.commune)
                listDep.append(e.etablissement.departement)
                statut_j.append(e.etablissement.statut_juridique)
                nom_etablissements.append(e.etablissement.nom_etablissement)
                lesFormationsNon.append(e.nom_formation)


        return sorted(set(lisReg)) ,sorted(set(lisCommune)),sorted(set(listDep)),sorted(set(statut_j)),sorted(set(nom_etablissements)),sorted(set(lesFormationsNon))
    def getRegions_one(formations):
        lisReg=[]
        listDep=[]
        lisCommune=[]
        statut_j=[]
        nom_etablissements=[]
        for e in formations:
            lisReg.append(e.etablissement.region)
            lisCommune.append(e.etablissement.commune)
            listDep.append(e.etablissement.departement)
            statut_j.append(e.etablissement.statut_juridique)
            nom_etablissements.append(e.etablissement.nom_etablissement)
            lesFormationsNon.append(e.nom_formation)
        
        return sorted(set(lisReg)) ,sorted(set(lisCommune)),sorted(set(listDep)),sorted(set(statut_j)),sorted(set(nom_etablissements)),sorted(set(lesFormationsNon))  
    req_commune=""
    req_departement=""
    req_region=""
    req_statu=""
    req_form_active=True
    req_nom_formation=""
    req_nom_etablissement=""
    mtype="initiale"
    
    etablissemnts=format_for_leaflet_b(formations,fm)
    regions,communes,departements,statuJur,nom_etablissements,lesFormationsNon=getRegions(formations,fm)
    if request.method=="POST": 
        req_departement=request.POST['departement']
        req_commune=request.POST['commune']
        req_region=request.POST['region']
        req_statu=request.POST['statut_juridique']
        req_nom_formation=request.POST['nom_formation']
        mtype=request.POST['type']
        req_nom_etablissement=request.POST['nom_etablissement']
        #si initial
        
        if req_nom_formation:
            req_form_active=True
        
            
        if mtype=='initiale':
            #filtre formation
            formations=Formation.objects.all().distinct('etablissement__id')
            if req_nom_formation:
                formations=Formation.objects.filter(nom_formation=req_nom_formation).distinct('etablissement__id')
                #formations=formations.filter(nom_formation=req_nom_formation)
            if req_region:
                formations=formations.filter(etablissement__region=req_region)
            if req_departement:
                formations=formations.filter(etablissement__departement=req_departement)
            if req_commune:
                formations=formations.filter(etablissement__commune=req_commune)
            if req_statu:
                formations=formations.filter(etablissement__statut_juridique=req_statu)
            if req_nom_etablissement:
                formations=formations.filter(etablissement__nom_etablissement__icontains=req_nom_etablissement)
            
            etablissemnts=format_for_leaflet(formations)
            regions,communes,departements,statuJur,nom_etablissements,lesFormationsNon=getRegions_one(formations)

        #si modulaire
        else:
            
            #filtre formation
            formations=Formation_modulaire.objects.all().distinct('etablissement__id')
            if req_nom_formation:
                formations=Formation_modulaire.objects.filter(nom_formation=req_nom_formation).distinct('etablissement__id')
                #formations=formations.filter(nom_formation=req_nom_formation)
            if req_region:
                formations=formations.filter(etablissement__region=req_region)
            if req_departement:
                formations=formations.filter(etablissement__departement=req_departement)
            if req_commune:
                formations=formations.filter(etablissement__commune=req_commune)
            if req_statu:
                formations=formations.filter(etablissement__statut_juridique=req_statu)
            if req_nom_etablissement:
                formations=formations.filter(etablissement__nom_etablissement__icontains=req_nom_etablissement)
            
            etablissemnts=format_for_leaflet(formations)
            regions,communes,departements,statuJur,nom_etablissements,lesFormationsNon=getRegions_one(formations)

        #etablissemnts_dj=EtablissemntsFilter(request.POST,etablissemnts_dj).qs
        
    
    list_nom_form=getFormation(formations)
    
    return render(request,'cartographie.html',{'etablissements':etablissemnts,'regions':regions,'communes':communes,
    'departements':departements,
    'nom_etablissements':nom_etablissements,
    'list_nom_form':list_nom_form,
    'statuJur':statuJur,
    'req_departement':req_departement,
    'req_commune':req_commune,
    'req_region':req_region,
    'articles_recents':articles_recents,
    'req_satatu':req_statu,
    'req_nom_formation':req_nom_formation,
    'lesFormationsNon':lesFormationsNon,
    'req_form_active':req_form_active,
    'req_nom_etablissement':req_nom_etablissement,
    'mtype':mtype,
    })
def demande(request):
    m_error=False
    message=False
    if request.method=='POST':
        forms=DemandeForms(request.POST)
        if forms.is_valid():
            forms.save()
            message=True
        else:
            forms=DemandeForms()
            m_error=True
            print(forms.errors)
    #home code
    formations=Formation.objects.all()
    formations_m=Formation_modulaire.objects.all()
    etablissemnts_dj=Etablissement.objects.all()
    nb_etablissement=len(etablissemnts_dj)
    nb_fromation=len(formations)+len(formations_m)
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
    # # if request.method=="POST":
    # #     req_departement=request.POST['departement']
    # #     req_commune=request.POST['commune']
    # #     req_region=request.POST['region']
        
    #     etablissemnts_dj=EtablissemntsFilter(request.POST,etablissemnts_dj).qs
    regions,communes,departements=getRegions(etablissemnts_dj)
    #article recents
    articles_recents=Article.objects.all().order_by('created_at')[:5]


    #formulaire demande 
    forms=DemandeForms()
    return render(request, 'index.html',{'etablissements':etablissemnts,'regions':regions,'communes':communes,
    'departements':departements,
    'req_departement':req_departement,
    'req_commune':req_commune,
    'req_region':req_region,
    'formations':formations,
    'nb_etablissement':nb_etablissement,
    'nb_formation':nb_fromation,
    'articles_recents':articles_recents,
    'forms':forms,
    'message':message,
    'm_error':m_error})
    #end code home


def home(request):
    formations=Formation.objects.all()
    formations_m=Formation_modulaire.objects.all()
    etablissemnts_dj=Etablissement.objects.all()
    nb_etablissement=len(etablissemnts_dj)
    nb_fromation=len(formations)+len(formations_m)
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


    #formulaire demande 
    forms=DemandeForms()
    return render(request, 'index.html',{'etablissements':etablissemnts,'regions':regions,'communes':communes,
    'departements':departements,
    'req_departement':req_departement,
    'req_commune':req_commune,
    'req_region':req_region,
    'formations':formations,
    'nb_etablissement':nb_etablissement,
    'nb_formation':nb_fromation,
    'articles_recents':articles_recents,
    'forms':forms,
    'message':False})



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
    formation=get_object_or_404(Formation,pk=id)

    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'detailsFormation.html',{'formation':formation,'articles_recents':articles_recents,'modulaire':'initiale'})
#details formations_modulaire
def detailFormationM(request,id):
    formation=get_object_or_404(Formation_modulaire,pk=id)

    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'detailsFormation.html',{'formation':formation,'articles_recents':articles_recents,'modulaire':'modulaire'})

#details formations
def detailEtablissement(request,id):
    print('=========================')
    etablissement=get_object_or_404(Etablissement,pk=id)
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
#a propos
def a_propos(request):
    articles_recents=Article.objects.all().order_by('created_at')[:5]
    return render(request,'apropos.html',{'articles_recents':articles_recents,})

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
    article=get_object_or_404(Article,pk=id)
   
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

