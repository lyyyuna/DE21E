from django.db import models
from django.contrib import admin

from draceditor.widgets import AdminDraceditorWidget

from .models import Article

class YourModelAdmin(admin.ModelAdmin):
    list_display = ('title',) 
    search_fields = ('title',)
    formfield_overrides = {
        models.TextField: {'widget': AdminDraceditorWidget},
    }

admin.site.register(Article, YourModelAdmin)