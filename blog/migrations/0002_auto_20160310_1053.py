# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-10 10:53
from __future__ import unicode_literals

import blog.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=blog.models.PhoneField(max_length=11),
        ),
    ]
