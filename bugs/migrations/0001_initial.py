# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 10:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BugCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Bug categories',
                'verbose_name': 'Bug category',
            },
        ),
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('os', models.CharField(blank=True, max_length=100, verbose_name='Operating system')),
                ('ram', models.CharField(blank=True, max_length=100, verbose_name='RAM')),
                ('gpu', models.CharField(blank=True, max_length=100, verbose_name='GPU')),
                ('cuda_cores', models.CharField(blank=True, max_length=100, verbose_name='CUDA cores')),
                ('vram', models.CharField(blank=True, max_length=100, verbose_name='Video RAM')),
                ('severity', models.SmallIntegerField(choices=[(1, 'Low'), (2, 'Normal'), (3, 'High'), (4, 'Urgent'), (5, 'Immediate')], default=2)),
                ('status', models.SmallIntegerField(choices=[(0, 'New'), (1, 'Master'), (2, 'Duplicate')], default=0)),
                ('is_solved', models.BooleanField(default=False)),
                ('project', models.CharField(blank=True, max_length=100, verbose_name='Project title')),
                ('particle', models.CharField(blank=True, max_length=100, verbose_name='Particle number')),
                ('triangle', models.CharField(blank=True, max_length=100, verbose_name='Triangle number')),
                ('description', models.TextField()),
                ('reproduce', models.TextField(blank=True, verbose_name='Steps to reproduce')),
                ('actual', models.TextField(blank=True, verbose_name='Actual behavior')),
                ('expected', models.TextField(blank=True, verbose_name='Expected behavior')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bugs.BugCategory')),
                ('master', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bugs.BugReport')),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Bug reports',
                'verbose_name': 'Bug report',
            },
        ),
    ]
