# Generated by Django 4.0.2 on 2022-04-29 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fachowiecApi', '0003_alter_worker_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='Rating',
        ),
        migrations.AddField(
            model_name='worker',
            name='rating',
            field=models.ManyToManyField(related_name='worker_rating', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='worker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='worker', to=settings.AUTH_USER_MODEL),
        ),
    ]