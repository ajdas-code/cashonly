# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-18 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_load_intial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesses',
            name='facebook_page',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='businesses',
            name='yelp_page',
            field=models.URLField(blank=True, null=True),
        ),
    ]
