from django.conf.urls import patterns, url
from brain_strain import views

urlpatterns = patterns('',
url(r'^$', views.index, name='index'),
url(r'^profile/$', views.profile, name='profile'),
url(r'^settings/$', views.settings, name='settings'),
url(r'^help/$', views.help, name='help'),
url(r'^start/$', views.start, name='start')
)
