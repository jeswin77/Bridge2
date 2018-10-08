# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-05 03:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0020_auto_20181003_0630'),
        ('tutor', '0005_tutornotes_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.ImageField(upload_to='media/tutorads')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Tutor')),
            ],
        ),
    ]