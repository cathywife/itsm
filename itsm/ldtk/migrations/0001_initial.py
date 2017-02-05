# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 20:47
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
            name='biaoqian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='fuwufanwei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fwfw_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='gongju',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='itsmsj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sjid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='itsmwt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wt_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='itsmzsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zsk_name', models.CharField(max_length=200)),
                ('zsk_chulifangfan', models.CharField(max_length=500)),
                ('zsk_jianyirenshu', models.IntegerField()),
                ('zsk_gongju', models.ManyToManyField(to='ldtk.gongju')),
                ('zsk_gongxianzhe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='jifang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='jigui',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jg_weizhi', models.CharField(max_length=100)),
                ('jg_jf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldtk.jifang')),
            ],
        ),
        migrations.CreateModel(
            name='peizhiku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pz_user', models.CharField(max_length=100)),
                ('pz_pwd', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='shebei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sb_jcsj', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='shebeileixin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sblx_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ug_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='weizhi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wz_shen', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='xjitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xjitem_name', models.CharField(max_length=100)),
                ('xjitem_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldtk.fuwufanwei')),
            ],
        ),
        migrations.CreateModel(
            name='yonghu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yh_name', models.CharField(max_length=50)),
                ('yh_psw', models.CharField(max_length=20)),
                ('yh_phone', models.IntegerField()),
                ('yh_address', models.CharField(max_length=100)),
                ('yh_descripition', models.CharField(max_length=100)),
                ('yh_birthday', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='yonghudanwei',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yhdw_name', models.CharField(max_length=100)),
                ('yhdw_address', models.CharField(max_length=100)),
                ('yhdw_Tel', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='yonghu',
            name='yh_dan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldtk.yonghudanwei'),
        ),
        migrations.AddField(
            model_name='shebei',
            name='sb_lx',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldtk.shebeileixin'),
        ),
        migrations.AddField(
            model_name='peizhiku',
            name='pz_iitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldtk.shebei'),
        ),
        migrations.AddField(
            model_name='jifang',
            name='jf_danwei',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldtk.yonghudanwei'),
        ),
        migrations.AddField(
            model_name='jifang',
            name='jf_gly',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldtk.yonghu'),
        ),
        migrations.AddField(
            model_name='jifang',
            name='jf_weizhi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldtk.weizhi'),
        ),
        migrations.AddField(
            model_name='itsmzsk',
            name='zsk_sblx',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ldtk.shebeileixin'),
        ),
    ]