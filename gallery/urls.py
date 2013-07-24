#encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('gallery.views',
    url(r'^(?P<pk>\d+)/$', 'album', name='gallery_album'),
)