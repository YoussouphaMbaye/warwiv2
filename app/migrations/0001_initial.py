# Generated by Django 3.1.7 on 2021-07-16 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nom_formation', models.CharField(blank=True, max_length=500, null=True)),
                ('region', models.CharField(blank=True, max_length=500, null=True)),
                ('departement', models.CharField(blank=True, max_length=500, null=True)),
                ('commune', models.CharField(blank=True, max_length=500, null=True)),
                ('ia', models.CharField(blank=True, max_length=500, null=True)),
                ('ief', models.CharField(blank=True, max_length=500, null=True)),
                ('adresse', models.CharField(blank=True, max_length=500, null=True)),
                ('longittude', models.CharField(blank=True, max_length=500, null=True)),
                ('lattitude', models.CharField(blank=True, max_length=500, null=True)),
                ('m_enseignant_sup', models.BooleanField(blank=True, default=0)),
                ('m_agriculture', models.BooleanField(blank=True, default=0)),
                ('m_formation', models.BooleanField(blank=True, default=0)),
                ('m_jeunesse', models.BooleanField(blank=True, default=0)),
                ('m_femme', models.BooleanField(blank=True, default=0)),
                ('m_autre', models.BooleanField(blank=True, default=0)),
                ('m_elevage', models.BooleanField(blank=True, default=0)),
                ('m_peche', models.BooleanField(blank=True, default=0)),
                ('m_si_autre', models.CharField(blank=True, max_length=500, null=True)),
                ('telephone', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('m_site_web', models.CharField(blank=True, max_length=500, null=True)),
                ('date_de_creation', models.CharField(blank=True, max_length=500, null=True)),
                ('statut_juridique', models.CharField(blank=True, max_length=500, null=True)),
                ('autre_statut_juridique', models.CharField(blank=True, max_length=500, null=True)),
                ('dc_nom', models.CharField(blank=True, max_length=500, null=True)),
                ('dc_genre', models.CharField(blank=True, max_length=500, null=True)),
                ('dc_email', models.CharField(blank=True, max_length=500, null=True)),
                ('dc_telephone', models.CharField(blank=True, max_length=500, null=True)),
                ('last_materiel', models.CharField(blank=True, max_length=500, null=True)),
                ('nb_salle', models.IntegerField(blank=True, default=0)),
                ('nb_atelier', models.IntegerField(blank=True, default=0)),
                ('autre_infrastructure', models.CharField(blank=True, max_length=500, null=True)),
                ('superfice_agricole', models.CharField(blank=True, max_length=500, null=True)),
                ('partenaire_structure', models.CharField(blank=True, max_length=500, null=True)),
                ('partenaire_principal', models.CharField(blank=True, max_length=500, null=True)),
                ('type_partenaire', models.CharField(blank=True, max_length=500, null=True)),
                ('partenaire_technique', models.CharField(blank=True, max_length=500, null=True)),
                ('partenaire_financier', models.CharField(blank=True, max_length=500, null=True)),
                ('existance_bd', models.CharField(blank=True, max_length=500, null=True)),
                ('nb_homme', models.IntegerField(blank=True, default=0)),
                ('nb_femme', models.IntegerField(blank=True, default=0)),
                ('auto_emploie_homme', models.IntegerField(blank=True, default=0)),
                ('auto_emploie_femme', models.IntegerField(blank=True, default=0)),
                ('emploie_partenaire', models.IntegerField(blank=True, default=0)),
                ('autre_apreciation', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nom_formation', models.CharField(blank=True, max_length=500, null=True)),
                ('niveau_requis', models.CharField(blank=True, max_length=500, null=True)),
                ('c_concours', models.BooleanField(blank=True, default=0)),
                ('c_dossier', models.BooleanField(blank=True, default=0)),
                ('c_autre', models.BooleanField(blank=True, default=0)),
                ('c_entretien', models.BooleanField(blank=True, default=0)),
                ('duree', models.CharField(blank=True, max_length=500, null=True)),
                ('nb_forme', models.IntegerField(blank=True, default=0)),
                ('nb_femme', models.IntegerField(blank=True, default=0)),
                ('d_dts', models.BooleanField(blank=True, default=0)),
                ('d_bts', models.BooleanField(blank=True, default=0)),
                ('d_bt', models.BooleanField(blank=True, default=0)),
                ('d_cs', models.BooleanField(blank=True, default=0)),
                ('d_bac', models.BooleanField(blank=True, default=0)),
                ('d_licence', models.BooleanField(blank=True, default=0)),
                ('d_master', models.BooleanField(blank=True, default=0)),
                ('d_doctorat', models.BooleanField(blank=True, default=0)),
                ('d_attestation', models.BooleanField(blank=True, default=0)),
                ('d_certificat', models.BooleanField(blank=True, default=0)),
                ('d_autre', models.BooleanField(blank=True, default=0)),
                ('d_cap', models.BooleanField(blank=True, default=0)),
                ('d_autre_nom', models.CharField(blank=True, max_length=500, null=True)),
                ('metier', models.CharField(blank=True, max_length=500, null=True)),
                ('accreditation', models.CharField(blank=True, max_length=500, null=True)),
                ('date_accreditation', models.CharField(blank=True, max_length=500, null=True)),
                ('structure_accreditation', models.CharField(blank=True, max_length=500, null=True)),
                ('habilitation', models.CharField(blank=True, max_length=500, null=True)),
                ('date_habilitation', models.CharField(blank=True, max_length=500, null=True)),
                ('structure_habilitation', models.CharField(blank=True, max_length=500, null=True)),
                ('cout_formation', models.CharField(blank=True, max_length=500, null=True)),
                ('nb_sortant_homme', models.IntegerField(blank=True, default=0)),
                ('nb_sortant_femme', models.IntegerField(blank=True, default=0)),
                ('etablissement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.etablissement')),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(blank=True, max_length=500, null=True)),
                ('prenom', models.CharField(blank=True, max_length=500, null=True)),
                ('categorie', models.CharField(blank=True, max_length=500, null=True)),
                ('qualification', models.CharField(blank=True, max_length=500, null=True)),
                ('domaine_specialisation', models.CharField(blank=True, max_length=500, null=True)),
                ('auto_domaine', models.CharField(blank=True, max_length=500, null=True)),
                ('etablissement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.etablissement')),
            ],
        ),
    ]
