# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptapp', '0005_auto_20151019_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fback',
            name='feedback',
            field=models.TextField(max_length=200),
        ),
    ]
