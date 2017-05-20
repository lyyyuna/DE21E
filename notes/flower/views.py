from django.shortcuts import render
from .models import Article


def index(request):
    article = Article.objects.order_by('createtime')[0]
    output = article.content
    return render(request, 'index.html', {'output': output})
