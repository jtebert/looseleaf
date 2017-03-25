# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.CharField(default=b'm4fnv7qaodvtffxx5p2bmptsrqkmqlaq', max_length=255, serialize=False, primary_key=True),
        ),
    ]
