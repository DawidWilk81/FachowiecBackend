# Generated by Django 4.0.2 on 2022-04-27 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0002_worker_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='age',
            field=models.PositiveIntegerField(),
        ),
    ]