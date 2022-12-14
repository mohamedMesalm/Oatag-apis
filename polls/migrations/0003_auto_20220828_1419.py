# Generated by Django 3.2.15 on 2022-08-28 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20220828_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='Playstore_config',
        ),
        migrations.RemoveField(
            model_name='config',
            name='appstore_config',
        ),
        migrations.AddField(
            model_name='appstore_config_class',
            name='appstore_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appstore', to='polls.config'),
        ),
        migrations.AddField(
            model_name='playstore_config_class',
            name='Playstore_config',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='playstore', to='polls.config'),
        ),
    ]
