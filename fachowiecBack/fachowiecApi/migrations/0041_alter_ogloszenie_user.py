# Generated by Django 4.0.2 on 2022-05-26 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fachowiecApi', '0040_alter_ogloszenie_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogloszenie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userAnnouncement', to=settings.AUTH_USER_MODEL),
        ),
    ]