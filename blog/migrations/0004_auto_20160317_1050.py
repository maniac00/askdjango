# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-17 10:50
from __future__ import unicode_literals

import askdjango.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160310_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=askdjango.fields.ImageField(default='', upload_to=askdjango.fields.random_name_upload_to),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jjal',
            name='image',
            field=askdjango.fields.ImageField(upload_to=askdjango.fields.random_name_upload_to),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]