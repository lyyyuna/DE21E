from django.db import models
from django.contrib import admin
from .models import OFile, OImage


class FileModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'createtime', 'get_url') 
    search_fields = ('title',)


class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'createtime', 'get_url') 
    search_fields = ('title',)


admin.site.register(OFile, FileModelAdmin)
admin.site.register(OImage, ImageModelAdmin)