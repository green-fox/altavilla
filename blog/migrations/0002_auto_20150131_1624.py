# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='width',
            field=models.IntegerField(default=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='height',
            field=models.IntegerField(default=30),
            preserve_default=True,
        ),
    ]
