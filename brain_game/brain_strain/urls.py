from django.conf.urls import patterns, url
from brain_strain import views

urlpatterns = patterns('',
url(r'^$', views.index, name='index'),
url(r'^profile/$', views.profile, name='profile'),
url(r'^get_help/$', views.get_help, name='get_help'),
url(r'^ajax/$', views.ajax, name='ajax'),
url(r'^players_list/$', views.players_list, name='players_list'),
url(r'^ajax_players/$', views.ajax_players, name='ajax_players'),
)
