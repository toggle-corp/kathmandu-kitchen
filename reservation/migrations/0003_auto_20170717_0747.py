# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_reservation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='reservation',
            name='special_request',
            field=models.TextField(blank=True, default=''),
        ),
    ]