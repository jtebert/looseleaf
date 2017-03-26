# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_auto_20170325_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='notebook',
            name='collaborators',
            field=models.ManyToManyField(related_name='collaborators', null=True, to='accounts.UserProfile', blank=True),
        ),
    ]
