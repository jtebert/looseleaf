from django.contrib import admin
from notes.models import Color, Note, Notebook

# Register your models here.

class ColorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Color, ColorAdmin)

class NoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Note, NoteAdmin)


class NotebookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Notebook, NotebookAdmin)