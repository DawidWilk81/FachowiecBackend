# Generated by Django 4.0.2 on 2022-05-05 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fachowiecApi', '0023_fachowiec_delete_pracownik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fachowiec',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fachowiec', to=settings.AUTH_USER_MODEL),
        ),
    ]
