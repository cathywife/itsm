# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtk', '0009_auto_20170205_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='itsmzsk',
            name='jianyirenshu',
            field=models.IntegerField(default=1),
        ),
    ]