# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('homeschool_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('response', models.BooleanField()),
                ('note', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='homeschooluser',
            name='status',
            field=models.CharField(help_text='The status of the user.', max_length=255, default='student', choices=[('student', 'Student'), ('alumni', 'Alumni'), ('chaperone', 'Chaperone')]),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
