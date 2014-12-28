from django.conf.urls import url, patterns, include
from Openworm import views, forms
from django.contrib.auth.models import User

urlpatterns = patterns('',
    url(r'^$', views.index, name='Home'),
)
