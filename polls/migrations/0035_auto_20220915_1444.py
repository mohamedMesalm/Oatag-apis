# Generated by Django 3.2.15 on 2022-09-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0034_alter_platforms_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='domain',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='platforms',
            name='domain',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]