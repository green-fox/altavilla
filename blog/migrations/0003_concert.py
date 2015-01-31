# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150131_1624'),
    ]

    operations = [
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
