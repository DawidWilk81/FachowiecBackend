# Generated by Django 4.0.2 on 2022-05-17 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0034_ogloszenie_opis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ogloszenie',
            old_name='opis',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='ogloszenie',
            old_name='tytul',
            new_name='title',
        ),
    ]