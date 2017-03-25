from __future__ import unicode_literals

from django.db import models

from accounts.models import UserProfile
from notes.utils import pkgen

from django_markdown.models import MarkdownField

# Create your models here.
# Let's add some functionality, bitches

class Color(models.Model):
    TEXT_COLOR_CHOICES = [
        ('dark', 'Dark'),
        ('light', 'Light'),
    ]

    name = models.CharField(max_length=127)
    hex = models.CharField(max_length=6)
    text_color = models.CharField(max_length=10, choices=TEXT_COLOR_CHOICES, default=0)

    def __str__(self):
        return self.name

class Notebook(models.Model):
    owner = models.ForeignKey(UserProfile)
    collaborators = models.ManyToManyField(UserProfile, related_name='collaborators', blank=True, null=True)
    title = models.CharField(max_length=255)
    color = models.ForeignKey(Color)

    def __str__(self):
        return self.title

class Note(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default=pkgen(32))
    notebook = models.ForeignKey(Notebook)
    # Note content
    content = MarkdownField(blank=True)
    # Positioning in grid
    x_pos = models.IntegerField()
    y_pos = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    # Other
    color = models.ForeignKey(Color)

    def __str__(self):
        return self.title