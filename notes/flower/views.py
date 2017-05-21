from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404 
from .models import Article, Tutorial, Course, Topic


def index(request):
    topics = Topic.objects.all()
    html_topics = []
    for topic in topics:
        html_topic = {
            'title':topic.title, 
            'slug':topic.slug, 
            'courses':topic.course_set.all()
            }
        html_topics.append(html_topic)
    return render(request, 'index.html', {'topics':html_topics})


def get_topic(request, topicslug):
    topic = get_object_or_404(Topic, slug=topicslug)
    courses = topic.course_set.all()
    return render(request, 'topic.html', {'topic':topic, 'courses':courses})


def get_course(request, courseslug):
    course = get_object_or_404(Course, slug=courseslug)
    tutorials = course.tutorial_set.all()

    html_tutorials = []
    for tutorial in tutorials:
        firstslug = None
        first_article = tutorial.article_set.order_by('createtime').first()
        if first_article is not None:
            firstslug = first_article.slug
 
        html_tutorial = {
            'title' : tutorial.title,
            'firstslug' : firstslug
        }
        html_tutorials.append(html_tutorial)

    return render(request, 'course.html', {'course':course, 'tutorials': html_tutorials})


def get_article(request, articleslug):
    article = get_object_or_404(Article, slug=articleslug)
    tutorial = article.tutorial
    articles = list(tutorial.article_set.order_by('createtime'))

    prev_slug = None
    next_slug = None

    try:
        index = articles.index(article)
    except:
        index = 0
    len_articles = len(articles)
    
    if len_articles == 1:
        prev_slug = None
        next_slug = None
    elif index == 0:
        next_slug = articles[1].slug
    elif index == len_articles-1:
        prev_slug = articles[-2].slug
    else:
        next_slug = articles[index+1].slug
        prev_slug = articles[index-1].slug

    return render(request, 'article.html', 
            {
                'title': article.title, 
                'content': article.content,
                'next_slug': next_slug,
                'prev_slug' : prev_slug,
                'tutorial_title' : tutorial.title,
                'articles' : articles,
                'currentslug' : articleslug
            })