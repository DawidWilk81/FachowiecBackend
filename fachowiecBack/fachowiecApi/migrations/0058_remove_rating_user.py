# Generated by Django 4.0.2 on 2022-07-14 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0057_rating_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
    ]
