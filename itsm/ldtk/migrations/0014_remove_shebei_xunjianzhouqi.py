# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 14:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ldtk', '0013_auto_20170216_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shebei',
            name='xunjianzhouqi',
        ),
    ]
