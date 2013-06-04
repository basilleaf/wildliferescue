from django.conf.urls import patterns, include, url
from rescue_map_app.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('rescue_map_app.views',
    url(r'^all.json', 'data_dump'),

    # Examples:
    # url(r'^$', 'rescue_map_project.views.home', name='home'),
    # url(r'^rescue_map_project/', include('rescue_map_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)
