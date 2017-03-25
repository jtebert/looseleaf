from django.conf.urls import patterns, include, url

from notes import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'add_note/$', views.add_note, name='add_note'),
    url(r'notebook/add/$', views.add_notebook, name='add_notebook'),
    url(r'^notebook/(?P<pk>\w+)/$', views.notebook, name='notebook'),
)