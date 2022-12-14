# Generated by Django 3.2.15 on 2022-09-17 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0035_auto_20220915_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200, null=True)),
                ('fontSize', models.CharField(blank=True, max_length=200, null=True)),
                ('fontName', models.CharField(blank=True, max_length=200, null=True)),
                ('fontType', models.CharField(blank=True, max_length=200, null=True)),
                ('fontColor', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True)),
                ('discount', models.CharField(blank=True, max_length=200, null=True)),
                ('payment', models.CharField(blank=True, max_length=200, null=True)),
                ('connection', models.CharField(blank=True, max_length=200, null=True)),
                ('report', models.CharField(blank=True, max_length=200, null=True)),
                ('info', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='html',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True)),
                ('info', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('fontSize', models.CharField(blank=True, max_length=200, null=True)),
                ('fontName', models.CharField(blank=True, max_length=200, null=True)),
                ('fontType', models.CharField(blank=True, max_length=200, null=True)),
                ('fontColor', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
