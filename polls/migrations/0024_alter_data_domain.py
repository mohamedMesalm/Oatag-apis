# Generated by Django 3.2.15 on 2022-09-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_remove_profile_favoritekey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='domain',
            field=models.URLField(max_length=128),
        ),
    ]
