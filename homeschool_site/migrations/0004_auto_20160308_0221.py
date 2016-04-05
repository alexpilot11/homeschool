# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeschool_site', '0003_auto_20160308_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='is_visible_by_unreg',
            field=models.BooleanField(verbose_name='Seen By Unapproved Users?'),
        ),
    ]
