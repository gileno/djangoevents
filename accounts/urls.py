#encoding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('accounts.views',
	url(r'^cadastro/$', 'signup', name='signup'),
)