from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^topic/(?P<topicslug>[\w-]+)/$', views.get_topic, name='topic_detail'),
    #url(r'^course/(?P<courseslug>[\w-]+)/$', views.get_course, name='course_detail'),
    url(r'^tutorial/(?P<articleslug>[\w-]+)/$', views.get_article, name='article_detail'),
    url(r'^$', views.index, name='index'),
]