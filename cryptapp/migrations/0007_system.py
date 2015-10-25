# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptapp', '0006_auto_20151019_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='system',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cipher', models.CharField(max_length=200)),
            ],
        ),
    ]
