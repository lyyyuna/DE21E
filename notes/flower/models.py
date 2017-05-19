from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=30, default='New')
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) 
    content = models.TextField()
    createtime = models.DateTimeField(auto_now=True)
    
    

