from django.conf.urls import patterns, include, url

from notes import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)