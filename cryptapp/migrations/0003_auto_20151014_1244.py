# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptapp', '0002_faq'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='faq',
            new_name='fback',
        ),
    ]
