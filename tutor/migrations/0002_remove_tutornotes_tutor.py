# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-03 05:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutornotes',
            name='tutor',
        ),
    ]