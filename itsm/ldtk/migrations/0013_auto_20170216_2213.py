# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ldtk', '0012_auto_20170216_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shebei',
            name='xunjianzhouqi',
            field=models.DurationField(default=10),
        ),
    ]
