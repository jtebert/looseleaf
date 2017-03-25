from django.contrib import admin
from notes.models import Color

# Register your models here.

class ColorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Color, ColorAdmin)