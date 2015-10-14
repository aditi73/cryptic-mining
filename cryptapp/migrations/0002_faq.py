# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cryptapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedback', models.CharField(max_length=200)),
                ('name', models.TextField(max_length=50)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
    ]
