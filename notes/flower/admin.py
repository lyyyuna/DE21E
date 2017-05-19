from django.db import models
from django.contrib import admin

from draceditor.widgets import AdminDraceditorWidget

from .models import Article

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'createtime') 
    search_fields = ('title',)
    formfield_overrides = {
        models.TextField: {'widget': AdminDraceditorWidget},
    }

admin.site.register(Article, ArticleModelAdmin)