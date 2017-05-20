from django.db import models
from django.contrib import admin

from draceditor.widgets import AdminDraceditorWidget

from .models import Article, Tutorial, Course, Topic

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'tutorial', 'createtime') 
    search_fields = ('title',)
    formfield_overrides = {
        models.TextField: {'widget': AdminDraceditorWidget},
    }


class TutorialModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'course') 
    search_fields = ('title',)


class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'topic') 
    search_fields = ('title',)


class TopicModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug') 
    search_fields = ('title',)


admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Tutorial, TutorialModelAdmin)
admin.site.register(Course, CourseModelAdmin)
admin.site.register(Topic, TopicModelAdmin)