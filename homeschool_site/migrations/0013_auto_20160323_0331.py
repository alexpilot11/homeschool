# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 03:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeschool_site', '0012_auto_20160323_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='time_rsvpd',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]