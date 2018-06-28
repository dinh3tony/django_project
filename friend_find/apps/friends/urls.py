from django.conf.urls import url
from . import views

urlpatterns = [

	url(r'^$', views.index),
	url(r'login/$', views.success),
	url(r'wall/$', views.wall),
	url(r'clear/$', views.clear),
	url(r'page/$', views.page),
	url(r'profile/$', views.profile, name = "profile"),
	url(r'gamble/$', views.gamble),
]