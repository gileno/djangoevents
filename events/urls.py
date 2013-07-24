#encoding: utf-8

from django.conf.urls import patterns, include, url

from .views import EventListView, EventDetailView

urlpatterns = patterns('events.views',
    url(r'^$', EventListView.as_view(), name='events'),
    url(r'^(?P<pk>\d+)/$', EventDetailView.as_view(), 
        name='events_details'),
    url(r'^novo-evento/$', 'create', name='events_create'),
    url(r'^meus-eventos/$', 'my', name='events_my'),
    url(r'^(?P<pk>\d+)/alterar/$', 'edit', name='events_edit'),
    url(r'^(?P<pk>\d+)/apagar/$', 'delete', name='events_delete'),
    url(r'^(?P<pk>\d+)/albuns/$', 'albums', name='events_albums'),
    url(r'^(?P<pk>\d+)/albuns/criar/$', 'create_album', 
        name='events_create_album'),
)