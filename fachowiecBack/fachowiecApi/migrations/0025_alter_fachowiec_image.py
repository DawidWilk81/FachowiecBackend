# Generated by Django 4.0.2 on 2022-05-05 19:28

from django.db import migrations, models
import fachowiecApi.models


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0024_alter_fachowiec_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fachowiec',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=fachowiecApi.models.upload_avatar),
        ),
    ]