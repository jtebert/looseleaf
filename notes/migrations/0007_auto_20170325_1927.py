# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20170325_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.CharField(default=b'fluy2j5t5ke3gb77yz26vm2ffckclalt', max_length=255, serialize=False, primary_key=True),
        ),
    ]
