# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-02 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsTiltApp', '0011_auto_20180728_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]