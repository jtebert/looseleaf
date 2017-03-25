# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20170325_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='text_color',
        ),
        migrations.AddField(
            model_name='color',
            name='text_color',
            field=models.CharField(default=0, max_length=10, choices=[(0, 'Dark'), (1, 'Light')]),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.CharField(default=b'6uaul6ixyemidmuj6dmx27kkgr5k6eln', max_length=255, serialize=False, primary_key=True),
        ),
    ]
