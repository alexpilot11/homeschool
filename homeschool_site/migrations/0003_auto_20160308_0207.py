# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeschool_site', '0002_auto_20160308_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterModelOptions(
            name='rsvp',
            options={'verbose_name': 'RSVP', 'verbose_name_plural': 'RSVPs'},
        ),
        migrations.AddField(
            model_name='rsvp',
            name='event',
            field=models.ForeignKey(to='homeschool_site.Event', null=True),
        ),
    ]
