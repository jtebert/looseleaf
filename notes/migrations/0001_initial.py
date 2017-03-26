# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170325_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=127)),
                ('hex', models.CharField(max_length=6)),
                ('text_color', models.CharField(default=0, max_length=10, choices=[('dark', 'Dark'), ('light', 'Light')])),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', django_markdown.models.MarkdownField(blank=True)),
                ('x_pos', models.IntegerField()),
                ('y_pos', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('color', models.ForeignKey(to='notes.Color')),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('collaborators', models.ManyToManyField(related_name='collaborators', null=True, to='accounts.UserProfile', blank=True)),
                ('color', models.ForeignKey(to='notes.Color')),
                ('owner', models.ForeignKey(to='accounts.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='notebook',
            field=models.ForeignKey(to='notes.Notebook'),
        ),
    ]
