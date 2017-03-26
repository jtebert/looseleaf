# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='collaborators',
            field=models.ManyToManyField(related_name='collaborators', to='accounts.UserProfile', blank=True),
        ),
    ]
