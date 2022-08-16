# Generated by Django 4.0.2 on 2022-04-30 15:39

from django.db import migrations, models
import fachowiecApi.models


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0007_worker_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='is_worker',
            field=models.BooleanField(default='none'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='Image',
            field=models.ImageField(blank=True, upload_to=fachowiecApi.models.upload_avatar),
        ),
    ]
