# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150131_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='songCloudCode_final',
            field=models.TextField(default='', editable=False),
            preserve_default=False,
        ),
    ]
