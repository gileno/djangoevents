from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

from core.views import HomeView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoevents.views.home', name='home'),
    # url(r'^djangoevents/', include('djangoevents.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^eventos/', include("events.urls")),
    url(r'^contas/', include("accounts.urls")),
    url(r'^galeria/', include("gallery.urls")),
    url(r'^entrar/$', "django.contrib.auth.views.login",
        {'template_name': 'login.html'}, name='login'),
    url(r'^sair/$', "django.contrib.auth.views.logout",
        {'next_page': '/'}, name='logout'),
    #url(r"^$", "core.views.home", name="home"),
    url(r"^$", HomeView.as_view(), name="home"),
    url(r"^fale-conosco/$", "core.views.contact", name="contact"),

    url(r'', include('social_auth.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.STATIC_ROOT}),
    )