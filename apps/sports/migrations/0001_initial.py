# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2022-02-01 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=6)),
                ('image', models.CharField(max_length=100)),
                ('sport', models.CharField(choices=[('basketball', 'Basketball'), ('football', 'Football'), ('baseball', 'Baseball'), ('cricket', 'Cricket'), ('hockey', 'Hockey')], default='basketball', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]