# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_auto_20170325_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.CharField(default=b'2g66pnq32n4lgufdirbexfe45xlegl6f', max_length=32, serialize=False, primary_key=True),
        ),
    ]
