# Generated by Django 3.2.15 on 2022-09-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_vcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vcard',
            name='vcf_file',
            field=models.FileField(blank=True, upload_to='Vcard'),
        ),
    ]
