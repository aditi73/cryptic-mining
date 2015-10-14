# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptapp', '0003_auto_20151014_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='fback',
            name='email',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
