# Generated by Django 3.1.7 on 2021-07-18 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210716_2347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='etablissement',
            old_name='m_site_web',
            new_name='site_web',
        ),
    ]
