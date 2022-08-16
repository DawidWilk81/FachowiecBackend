# Generated by Django 4.0.2 on 2022-05-05 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import fachowiecApi.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fachowiecApi', '0022_pracownik_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fachowiec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='Jestem najlepszy w swojej dziedzinie', max_length=366)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to=fachowiecApi.models.upload_avatar)),
                ('category', models.CharField(blank=True, default='brak', max_length=128, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('is_worker', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Pracownik',
        ),
    ]
