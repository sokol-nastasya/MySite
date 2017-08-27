from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^about/$', views.about, name = 'about' ),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.show_article, name = 'show_article'),
    url(r'^article/addcomment(?P<article_id>[0-9]+)/$', views.addcomment, name = 'addcomment')

]
