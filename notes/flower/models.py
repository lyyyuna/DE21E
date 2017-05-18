from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20, default='New')
    content = models.TextField()
