from django.conf.urls import patterns, include, url

from notes import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'get_notes/$', views.get_notes, name='get_notes'),
    url(r'add_note/$', views.add_note, name='add_note'),
    url(r'edit_note/$', views.edit_note, name='edit_note'),
    url(r'move_notes/$', views.move_notes, name='move_notes'),
    url(r'delete_note/$', views.delete_note, name='delete_note'),
    url(r'notebook/add/$', views.add_notebook, name='add_notebook'),
    url(r'^notebook/(?P<pk>\w+)/$', views.notebook, name='notebook'),
)