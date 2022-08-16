# Generated by Django 4.0.2 on 2022-07-10 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fachowiecApi', '0047_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='commentValue',
            field=models.TextField(default='Polecam', max_length=254),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userCommented', to='fachowiecApi.fachowiec'),
        ),
    ]
