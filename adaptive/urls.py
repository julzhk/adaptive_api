from django.conf import settings
from django.conf.urls import patterns, include, url
from message_api.views import index, coke_list, user_details
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adaptive.views.home', name='home'),
    # url(r'^adaptive/', include('adaptive.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^coke_list', coke_list, name='coke_list_page'),
    url(r'^user_details', user_details, name='user_details'),
    url(r'', index, name='index'),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
