# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptapp', '0004_fback_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fback',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
