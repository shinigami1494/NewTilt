# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-07 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsTiltApp', '0007_action_date_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='muser',
            name='categories',
            field=models.ManyToManyField(to='NewsTiltApp.Category'),
        ),
    ]
