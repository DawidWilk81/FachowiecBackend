# Generated by Django 4.0.2 on 2022-05-05 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0021_remove_pracownik_category_alter_pracownik_is_worker_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pracownik',
            name='category',
            field=models.CharField(blank=True, default='brak', max_length=128, null=True),
        ),
    ]