# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_group_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_member',
            name='descritpion',
            field=models.TextField(max_length=1000),
            preserve_default=True,
        ),
    ]
