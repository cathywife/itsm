# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 07:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ldtk', '0007_itsmzsk_gongxianzhe'),
    ]

    operations = [
        migrations.AddField(
            model_name='itsmzsk',
            name='shebei',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ldtk.shebei'),
        ),
    ]