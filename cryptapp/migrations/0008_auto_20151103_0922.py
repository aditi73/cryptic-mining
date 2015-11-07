# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cryptapp', '0007_system'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='result',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='system',
            name='cipher',
            field=models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(b'^[A-Za-z ]*$', b'Only contain alphabets')]),
        ),
    ]
