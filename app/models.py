from django.db import models

from ckeditor.fields import RichTextField
# Create your models here.
class Etablissement(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nom_etablissement=models.CharField(max_length=500,blank=True,null=True,verbose_name="nom de l'établissement")
    region=models.CharField(max_length=500,blank=True,null=True,verbose_name='région')
    departement=models.CharField(max_length=500,blank=True,null=True)
    commune=models.CharField(max_length=500,blank=True,null=True)
    ia=models.CharField(max_length=500,blank=True,null=True)
    ief=models.CharField(max_length=500,blank=True,null=True)
    adresse=models.CharField(max_length=500,blank=True,null=True)
    longitude=models.CharField(max_length=500,blank=True,null=True)
    latitude=models.CharField(max_length=500,blank=True,null=True)

    m_enseignant_sup=models.BooleanField(default=0,blank=True,null=True,verbose_name="ministére enseignement superieur")
    m_agriculture=models.BooleanField(default=0,blank=True,null=True,verbose_name="ministére agriculture")
    m_formation=models.BooleanField(default=0,blank=True,null=True ,verbose_name="ministére formation professionnelle")
    m_jeunesse=models.BooleanField(default=0,blank=True,null=True ,verbose_name="ministére femme")
    m_femme=models.BooleanField(default=0,blank=True,null=True ,verbose_name="ministére jeunesse")
    m_autre=models.BooleanField(default=0,blank=True,null=True ,verbose_name="ministére autre")
    m_elevage=models.BooleanField(default=0,blank=True,null=True ,verbose_name="ministére élevage")
    m_peche=models.BooleanField(default=0,blank=True,null=True ,verbose_name="ministére de pêche")
    m_si_autre=models.CharField(max_length=500,blank=True,null=True ,verbose_name="nom autre ministére")

    telephone=models.CharField(max_length=500,blank=True,null=True ,verbose_name="téléphone")
    email=models.CharField(max_length=500,blank=True,null=True)
    site_web=models.CharField(max_length=500,blank=True,null=True)
    date_de_creation=models.CharField(max_length=500,blank=True,null=True ,verbose_name="date de création")
    statut_juridique=models.CharField(max_length=500,blank=True,null=True)
    autre_statut_juridique=models.CharField(max_length=500,blank=True,null=True)

    dc_nom=models.CharField(max_length=500,blank=True,null=True ,verbose_name="nom représentant")
    dc_genre=models.CharField(max_length=500,blank=True,null=True ,verbose_name="genre représentant")
    dc_email=models.CharField(max_length=500,blank=True,null=True ,verbose_name="email représentant")
    dc_telephone=models.CharField(max_length=500,blank=True,null=True ,verbose_name="téléphone représentant")
    liste_materiel=models.TextField(blank=True,null=True)
    nb_salle=models.IntegerField(default=0,blank=True,null=True)
    nb_atelier=models.IntegerField(default=0,blank=True,null=True)
    autre_infrastructure=models.CharField(max_length=500,blank=True,null=True)
    superficie_agricole=models.CharField(max_length=500,blank=True,null=True)
    partenaire_structure=models.CharField(max_length=500,blank=True,null=True)
    partenaire_principal=models.CharField(max_length=500,blank=True,null=True)

    partenaire_technique=models.BooleanField(default=0,blank=True,null=True)
    partenaire_financier=models.BooleanField(default=0,blank=True,null=True)
    existance_bd=models.CharField(max_length=500,blank=True,null=True ,verbose_name="existance base de données")

    nb_homme=models.IntegerField(default=0,blank=True,null=True)
    nb_femme=models.IntegerField(default=0,blank=True,null=True)
    auto_emploie_homme=models.IntegerField(default=0,blank=True,null=True)
    auto_emploie_femme=models.IntegerField(default=0,blank=True,null=True)
    emploie_partenaire=models.IntegerField(default=0,blank=True,null=True)
    autre_apreciation=models.TextField(blank=True,null=True ,verbose_name="autre apréciation")

    created_at=models.DateTimeField(auto_now_add=True,null=True ,verbose_name="crée le")
    update_at=models.DateTimeField(auto_now=True,null=True ,verbose_name="mise à jour")
    def __str__(self):
        return  self.nom_etablissement



class Formation(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nom_formation=models.CharField(max_length=500,blank=True,null=True)
    niveau_requis=models.CharField(max_length=500,blank=True,null=True)

    c_concours=models.BooleanField(default=0,blank=True,null=True ,verbose_name="accès concours")
    c_dossier=models.BooleanField(default=0,blank=True,null=True ,verbose_name="accès dossier")
    c_autre=models.BooleanField(default=0,blank=True,null=True ,verbose_name="accès autre")
    c_autre_nom=models.CharField(max_length=500,blank=True,null=True ,verbose_name="nom autre accès")
    c_entretien=models.BooleanField(default=0,blank=True,null=True ,verbose_name="accès entretien")

    duree=models.CharField(max_length=500,blank=True,null=True)
    nb_homme=models.IntegerField(default=0,blank=True,null=True)
    nb_femme=models.IntegerField(default=0,blank=True,null=True)

    d_dts=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme DTS")
    d_bts=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme BTS")
    d_bt=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme BT")
    d_cs=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme CS")
    d_bac=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme BAC")
    d_licence=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme LICENCE")
    d_master=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme MASTER")
    d_doctorat=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme DOCTORAT")
    d_attestation=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme ATTESTATION")
    d_certificat=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme CERTIFICAT")
    d_autre=models.BooleanField(default=0,blank=True,null=True ,verbose_name="autre diplôme")
    d_cap=models.BooleanField(default=0,blank=True,null=True ,verbose_name="diplôme CAP")
    d_autre_nom=models.CharField(max_length=500,blank=True,null=True ,verbose_name="diplôme autre nom")
    
    metier=models.CharField(max_length=500,blank=True,null=True)
    accreditation=models.CharField(max_length=500,blank=True,null=True)
    date_accreditation=models.CharField(max_length=500,blank=True,null=True)
    structure_accreditation=models.CharField(max_length=500,blank=True,null=True)
    
    habilitation=models.CharField(max_length=500,blank=True,null=True)
    date_habilitation=models.CharField(max_length=500,blank=True,null=True)
    structure_habilitation=models.CharField(max_length=500,blank=True,null=True)

    cout_formation=models.CharField(max_length=500,blank=True,null=True ,verbose_name="coût formation")
    
    nb_sortant_homme=models.IntegerField(default=0,blank=True,null=True)
    nb_sortant_femme=models.IntegerField(default=0,blank=True,null=True)

    etablissement=models.ForeignKey(Etablissement,on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True,null=True ,verbose_name="crée le")
    update_at=models.DateTimeField(auto_now=True,null=True ,verbose_name="mise à jour")
    class Meta:
        verbose_name='Formation initiale'
        verbose_name_plural='Formations initiales'
    def __str__(self):
        return  self.nom_formation
#=============formatiom Modulaire===============
class Formation_modulaire(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nom_formation=models.CharField(max_length=500,blank=True,null=True)
    niveau_requis=models.CharField(max_length=500,blank=True,null=True)

    c_concours=models.BooleanField(default=0,blank=True,null=True ,verbose_name="accès concours")
    c_dossier=models.BooleanField(default=0,blank=True,null=True ,verbose_name="accès dossier")
    c_autre=models.BooleanField(default=0,blank=True,null=True ,verbose_name="accès autre")
    c_autre_nom=models.CharField(max_length=500,blank=True,null=True ,verbose_name="nom autre accès")
    c_entretien=models.BooleanField(default=0,blank=True,null=True ,verbose_name="accès entretien")

    duree=models.CharField(max_length=500,blank=True,null=True)
    nb_homme=models.IntegerField(default=0,blank=True,null=True)
    nb_femme=models.IntegerField(default=0,blank=True,null=True)

    diplome=models.CharField(max_length=500,blank=True,null=True,verbose_name="diplôme")
    
    metier=models.CharField(max_length=500,blank=True,null=True)
    accreditation=models.CharField(max_length=500,blank=True,null=True)
    date_accreditation=models.CharField(max_length=500,blank=True,null=True)
    structure_accreditation=models.CharField(max_length=500,blank=True,null=True)
    
    habilitation=models.CharField(max_length=500,blank=True,null=True)
    date_habilitation=models.CharField(max_length=500,blank=True,null=True)
    structure_habilitation=models.CharField(max_length=500,blank=True,null=True)

    cout_formation=models.CharField(max_length=500,blank=True,null=True ,verbose_name="coût formation")
    
    nb_sortant_homme=models.IntegerField(default=0,blank=True,null=True)
    nb_sortant_femme=models.IntegerField(default=0,blank=True,null=True)

    etablissement=models.ForeignKey(Etablissement,on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True,null=True ,verbose_name="crée le")
    update_at=models.DateTimeField(auto_now=True,null=True ,verbose_name="mise à jour")
    class Meta:
        verbose_name='Formation modulaire'
        verbose_name_plural='Formations modulaires'
    def __str__(self):
        return  self.nom_formation

#=====================================
class Employer(models.Model):
    id=models.BigIntegerField(primary_key=True)
    nom=models.CharField(max_length=500,blank=True,null=True)
    prenom=models.CharField(max_length=500,blank=True,null=True)
    categorie=models.CharField(max_length=500,blank=True,null=True)
    qualification=models.CharField(max_length=500,blank=True,null=True)
    domaine_specialisation=models.CharField(max_length=500,blank=True,null=True)
    auto_domaine=models.CharField(max_length=500,blank=True,null=True,verbose_name="autre domaine")

    etablissement=models.ForeignKey(Etablissement,on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True,null=True ,verbose_name="crée le")
    update_at=models.DateTimeField(auto_now=True,null=True ,verbose_name="mise à jour")
    class Meta:
        verbose_name='Employé'
        verbose_name_plural='Employés'
    def __str__(self):
        return  self.prenom+' '+self.nom

class Article(models.Model):
    titre=models.CharField(max_length=500,blank=True,null=True)
    contenu=RichTextField(blank=True,null=True)
    tags=models.CharField(max_length=500,blank=True,null=True)
    img_article = models.FileField(upload_to='imgArticle/')
    
    created_at=models.DateTimeField(auto_now_add=True,null=True ,verbose_name="crée le")
    update_at=models.DateTimeField(auto_now=True,null=True ,verbose_name="mise à jour")
    def __str__(self):
        return  self.titre


class Demande(models.Model):
    nom_etablissement=models.CharField(max_length=500,blank=False,null=True)
    email=models.EmailField(blank=False,null=True)
    telephone=models.CharField(max_length=500,blank=False,null=True)
    nom_ref=models.CharField(max_length=500,blank=False,null=True)
    message=models.TextField(max_length=400,blank=False,null=True)


