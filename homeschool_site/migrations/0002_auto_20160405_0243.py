# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 02:43
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeschool_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'About Us',
                'verbose_name': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_message', models.TextField(help_text='This will be your greeting message on the Contact Us page.')),
                ('contact_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254, null=True)),
                ('contact_phone', models.CharField(max_length=12, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits', regex='^\\d{10}$')])),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255, null=True)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('description', models.TextField(null=True)),
                ('other_info', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('time_of_news', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='RSVP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.BooleanField()),
                ('note', models.TextField()),
                ('num_guests', models.IntegerField()),
                ('time_rsvpd', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homeschool_site.Event')),
            ],
            options={
                'verbose_name_plural': 'RSVPs',
                'verbose_name': 'RSVP',
            },
        ),
        migrations.AddField(
            model_name='homeschooluser',
            name='status',
            field=models.CharField(choices=[('student', 'Student'), ('alumni', 'Alumni'), ('chaperone', 'Chaperone')], default='student', help_text='The status of the user.', max_length=255),
        ),
        migrations.AlterField(
            model_name='form',
            name='is_visible_by_unreg',
            field=models.BooleanField(verbose_name='Seen By Unapproved Users?'),
        ),
        migrations.AlterField(
            model_name='homeschooluser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username'),
        ),
        migrations.AddField(
            model_name='rsvp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
