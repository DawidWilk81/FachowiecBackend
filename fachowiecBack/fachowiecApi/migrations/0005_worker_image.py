# Generated by Django 4.0.2 on 2022-04-29 13:00

from django.db import migrations, models
import fachowiecApi.models


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0004_remove_worker_rating_worker_rating_alter_worker_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='Image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=fachowiecApi.models.upload_avatar),
        ),
    ]
