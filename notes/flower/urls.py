from django.conf.urls import url
from . import views
from .views import IndexView, ArticleView
from . import customuploader_views
from django.views.decorators.cache import cache_page


urlpatterns = [
    #url(r'^topic/(?P<topicslug>[\w-]+)/$', views.get_topic, name='topic_detail'),
    #url(r'^course/(?P<courseslug>[\w-]+)/$', views.get_course, name='course_detail'),
    url(r'^tutorial/(?P<articleslug>[\w-]+)/$', cache_page(60 * 15)(ArticleView.as_view()), name='article_detail'),
    url(r'^$', cache_page(60 * 15)(IndexView.as_view()), name='index'),
    url(r'^api/uploader/$', customuploader_views.markdown_uploader, name='markdown_uploader_page'),
]