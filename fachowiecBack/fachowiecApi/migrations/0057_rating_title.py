# Generated by Django 4.0.2 on 2022-07-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0056_alter_rating_pracownik'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='title',
            field=models.CharField(default='Najlepszy fachowiec', max_length=128),
        ),
    ]
