from __future__ import unicode_literals

from django.db import models

from accounts.models import UserProfile
from notes.utils import pkgen

# Create your models here.
# Let's add some functionality, bitches

class Color(models.Model):
    name = models.CharField(max_length=127)
    hex = models.CharField(max_length=6)

class Notebook(models.Model):
    owner = models.ForeignKey(UserProfile)
    collaborators = models.ManyToManyField(UserProfile, related_name='collaborators')
    title = models.CharField(max_length=255)
    color = models.ForeignKey(Color)

class Note(models.Model):
    id = models.CharField(max_length=255, primary_key=True, default=pkgen(255))
    notebook = models.ForeignKey(Notebook)
    # Note content
    title = models.CharField(max_length=255, blank=True)
    note_content = models.TextField(blank=True)
    # Positioning in grid
    x_pos = models.IntegerField()
    y_pos = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    # Other
    color = models.ForeignKey(Color)