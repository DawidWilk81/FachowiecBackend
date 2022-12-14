# Generated by Django 4.0.2 on 2022-05-16 19:12

from django.db import migrations, models
import fachowiecApi.models


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0029_alter_ogloszenie_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='ogloszenie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=fachowiecApi.models.upload_announcement_image),
        ),
        migrations.AddField(
            model_name='ogloszenie',
            name='phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ogloszenie',
            name='town',
            field=models.TextField(default='brak', max_length=64),
        ),
    ]
