from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.login, name = "login"),
	url(r'register/$', views.register, name = "register"),
	url(r'add_user/$', views.add_user, name = "profile"),
	url(r'profile/$', views.profile, name = "profile"),
	url(r'roll/$', views.roll, name = "roll"),
	url(r'dice/$', views.dice, name = "dice"),
]