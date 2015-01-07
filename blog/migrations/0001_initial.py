# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=2500, blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('video_code', models.CharField(max_length=2500, blank=True)),
                ('upload', models.ImageField(upload_to=b'images/', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name=b'Date du concert (*) :')),
                ('paf', models.DecimalField(null=True, verbose_name=b'Prix place  :', max_digits=5, decimal_places=0, blank=True)),
                ('description', models.CharField(max_length=50, verbose_name=b'Details (*) :')),
                ('place', models.CharField(max_length=50, verbose_name=b'Lieu (*) :')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
