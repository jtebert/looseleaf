# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0007_auto_20170325_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.CharField(default=b'bn4heys5m2y2ieaidhvqj4boxgwcczvk', max_length=32, serialize=False, primary_key=True),
        ),
    ]
