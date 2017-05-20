from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=30, default='New')
    createtime = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) 
    content = models.TextField()

    
    

