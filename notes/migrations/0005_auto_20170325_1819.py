# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20170325_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='text_color',
            field=models.CharField(default=0, max_length=10, choices=[('dark', 'Dark'), ('light', 'Light')]),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.CharField(default=b'pdq5hscubfm4hr4wk6mkpztzu4bipfie', max_length=255, serialize=False, primary_key=True),
        ),
    ]
