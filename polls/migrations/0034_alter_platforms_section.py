# Generated by Django 3.2.15 on 2022-09-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0033_alter_platforms_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platforms',
            name='section',
            field=models.CharField(choices=[('1', 'Social media'), ('2', 'Contact info'), ('3', 'For Business'), ('4', 'Payments'), ('5', 'Content'), ('6', 'Music'), ('7', 'More')], max_length=50),
        ),
    ]
