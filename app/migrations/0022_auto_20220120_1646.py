# Generated by Django 3.1.7 on 2022-01-20 15:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_demande_nom_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
