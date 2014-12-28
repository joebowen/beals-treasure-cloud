from django.conf.urls import url, patterns, include
from BealsTreasure import views
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^$', views.index, name='Home'),
    url(r'^status/$', views.status, name='Status'),
    url(r'^faq/$', views.faq, name='FAQ'),
    url(r'^about/$', views.about, name='About'),
    url(r'^contact/$', views.contact, name='Contact'),
)
