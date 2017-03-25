# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0008_auto_20170325_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.CharField(default=b'preqewjaag7bu63o47knyly6s4cp3g6n', max_length=32, serialize=False, primary_key=True),
        ),
    ]
