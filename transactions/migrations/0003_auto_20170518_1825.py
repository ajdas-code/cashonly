# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-18 22:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_bill_tip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='tip',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tip amount (in cents)'),
        ),
    ]
