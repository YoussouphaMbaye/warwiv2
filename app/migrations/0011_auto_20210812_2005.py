# Generated by Django 3.1.7 on 2021-08-12 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20210812_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etablissement',
            name='liste_materiel',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
