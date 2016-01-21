# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptapp', '0008_auto_20160116_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default=b'', max_length=100)),
                ('message', models.TextField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
