# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20170325_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='note_content',
        ),
        migrations.RemoveField(
            model_name='note',
            name='title',
        ),
        migrations.AddField(
            model_name='note',
            name='content',
            field=django_markdown.models.MarkdownField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.CharField(default=b'akme6yrsg2337cr45m76qaqh6aygjl7l', max_length=255, serialize=False, primary_key=True),
        ),
    ]
