from django.contrib import admin
from notes.models import Color, Note

# Register your models here.

class ColorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Color, ColorAdmin)

class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note, NoteAdmin)