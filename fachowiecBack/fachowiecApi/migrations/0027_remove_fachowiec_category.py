# Generated by Django 4.0.2 on 2022-05-07 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0026_remove_fachowiec_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fachowiec',
            name='category',
        ),
    ]
