from django.conf.urls.defaults import *

# from django.conf.urls import patterns, url, include

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'home.views.index'),
	(r'^pick/', 'confirm.views.confirm'),
    (r'^login/$', 'auth.views.login_user'),
    (r'^admin/', include(admin.site.urls)),
)