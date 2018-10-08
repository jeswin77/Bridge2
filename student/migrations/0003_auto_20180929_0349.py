# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-29 03:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_auto_20180929_0347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor_likes',
            name='user',
        ),
        migrations.AddField(
            model_name='tutor_likes',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
