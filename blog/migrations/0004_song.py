# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_concert'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_title', models.CharField(max_length=100)),
                ('songCloudCode', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
