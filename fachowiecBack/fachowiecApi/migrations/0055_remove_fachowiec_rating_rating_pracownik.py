# Generated by Django 4.0.2 on 2022-07-14 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0054_rating_delete_ocena'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fachowiec',
            name='rating',
        ),
        migrations.AddField(
            model_name='rating',
            name='pracownik',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fachowiecApi.fachowiec'),
        ),
    ]
