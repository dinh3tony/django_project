from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
	url(r'^$', views.login),

=======
	url(r'profile/$', views.profile, name = "profile"),
>>>>>>> ce0f850f09e09352cdfd8f27529f5cc43a565d3b
]