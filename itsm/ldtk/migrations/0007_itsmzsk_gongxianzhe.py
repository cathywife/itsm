# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 06:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ldtk', '0006_shebei_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='itsmzsk',
            name='gongxianzhe',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
