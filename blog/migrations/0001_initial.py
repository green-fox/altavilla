# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


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
                ('upload', sorl.thumbnail.fields.ImageField(upload_to=b'')),
                ('height', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
