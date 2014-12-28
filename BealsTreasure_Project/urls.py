from django.conf.urls import patterns, include, url
from django.contrib import admin
from BealsTreasure import urls as BealsTreasure

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BealsTreasure1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include(BealsTreasure)),
)
