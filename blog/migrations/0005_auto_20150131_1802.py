# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='songCloudCode',
            field=models.TextField(max_length=2000),
            preserve_default=True,
        ),
    ]
