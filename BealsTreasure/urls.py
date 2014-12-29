from django.conf.urls import url, patterns, include
from BealsTreasure import views
from django.contrib.auth.models import User
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='Home'),
    url(r'^status/$', views.status, name='Status'),
    url(r'^faq/$', views.faq, name='Frequently Asked Questions'),
    url(r'^about/$', views.about, name='About'),
    url(r'^contact/$', views.contact, name='Contact'),

    url(r'^faq/prize/$', views.faq_prize, name='Prize'),
    url(r'^faq/conjecture-what/$', views.faq_conjecture_what, name='What is Beal\'s Conjecture?'),
    url(r'^faq/what-if-conjecture-true/$', views.faq_what_if_conjecture_true, name='What if Conjecture is True?'),
    url(r'^faq/why-do-you-need-me/$', views.faq_why_do_you_need_me, name='Why do you need my help in the search?'),
    url(r'^faq/will-slow-down-my-computer/$', views.faq_will_slow_down_my_computer, name='Will this slow down my computer and/or network?'),
    url(r'^faq/download-data/$', views.faq_download_data, name='Why does this project first need to download data?'),
    url(r'^faq/are-you-a-hacker/$', views.faq_are_you_a_hacker, name='Is this project stealing my information? Or doing anything bad?'),
    url(r'^faq/do-i-need-to-know-math/$', views.faq_do_i_need_to_know_math, name='Do I need to know math?'),
    url(r'^faq/how-can-i-join/$', views.faq_how_can_i_join, name='How can I join?'),
    url(r'^faq/i-found-something/$', views.faq_i_found_something, name='I think I found something!  What happens now?'),
    url(r'^faq/donations/$', views.faq_donations, name='Can I donate to the project?'),

    url(r'^getwork$', views.getwork, name='getwork'),

    url(r'^populate$', views.Populate, name='Populate'),
)

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'data/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
