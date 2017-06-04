from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404 
from .models import Article, Tutorial, Course


# def index(request):
#     topics = Topic.objects.all()
#     html_topics = []
#     for topic in topics:
#         html_topic = {
#             'title':topic.title, 
#             'slug':topic.slug, 
#             'courses':topic.course_set.all()
#             }
#         html_topics.append(html_topic)
#     return render(request, 'index.html', {'topics':html_topics})


# def get_topic(request, topicslug):
#     topic = get_object_or_404(Topic, slug=topicslug)
#     courses = topic.course_set.all()
#     return render(request, 'topic.html', {'topic':topic, 'courses':courses})


def index(request):
    courses = Course.objects.all()
    html_courses = []
    for course in courses:
        html_course = {
            'title' : course.title,
            'tutorials' : get_course(course.id)
        }
        html_courses.append(html_course)

    return render(request, 'index.html', {'courses' : html_courses})


def get_course(id):
    course = get_object_or_404(Course, pk=id)
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

    return html_tutorials


def get_same_course_tutorial(tutorial):
    course = tutorial.course
    return get_course(course.id)[:5]


def get_latest_article():
    return Article.objects.all().order_by('-createtime')[:10]


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

    navigation_tutorials = get_same_course_tutorial(tutorial)
    latest_articles = get_latest_article()

    return render(request, 'article.html', 
            {
                'title': article.title, 
                'content': article.content,
                'next_slug': next_slug,
                'prev_slug' : prev_slug,
                'tutorial_title' : tutorial.title,
                'articles' : articles,
                'currentslug' : articleslug,
                'navigation_tutorials' : navigation_tutorials,
                'latest_articles' : latest_articles
            })