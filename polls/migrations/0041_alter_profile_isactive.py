# Generated by Django 3.2.15 on 2022-09-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0040_profile_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
