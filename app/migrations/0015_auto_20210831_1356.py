# Generated by Django 3.1.7 on 2021-08-31 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210830_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formation_modulaire',
            old_name='attestation',
            new_name='diplome',
        ),
    ]
