# Generated by Django 3.1.7 on 2021-08-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210811_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etablissement',
            name='nb_atelier',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='etablissement',
            name='nb_femme',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='etablissement',
            name='nb_homme',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='etablissement',
            name='nb_salle',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='formation',
            name='nb_sortant_femme',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='formation',
            name='nb_sortant_homme',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
