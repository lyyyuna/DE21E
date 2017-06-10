from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# class Topic(models.Model):
#     title = models.CharField(max_length=30, default='New')
#     slug = models.SlugField(default='New', unique=True, db_index=True)
#     createtime = models.DateTimeField(default=timezone.now, db_index=True)
#     description = models.CharField(max_length=100, default='New')

#     def __str__(self):
#         return self.title


class Course(models.Model):
    title = models.CharField(max_length=30, default='New')
    #slug = models.SlugField(default='New', unique=True, db_index=True)
    createtime = models.DateTimeField(default=timezone.now, db_index=True)
    description = models.CharField(max_length=100, default='New')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['createtime']


class Tutorial(models.Model):
    title = models.CharField(max_length=30, default='New')
    #slug = models.SlugField(default='New', unique=True, db_index=True)
    imgurl = models.URLField(default='someurl')
    createtime = models.DateTimeField(default=timezone.now, db_index=True)
    course = models.ForeignKey(Course, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=25, default='New')

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['createtime']


class Article(models.Model):
    title = models.CharField(max_length=30, default='New', db_index=True)
    slug = models.SlugField(default='New', unique=True, db_index=True)
    createtime = models.DateTimeField(default=timezone.now, db_index=True)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    tutorial = models.ForeignKey(Tutorial, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=100, default='New')
    content = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['createtime']