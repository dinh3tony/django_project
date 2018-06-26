from django.shortcuts import render, HttpResponse, redirect
<<<<<<< HEAD

def login(request):
	return render(request, "friends/login.html")
=======
from django.core.urlresolvers import reverse

# Create your views here.

def profile(request):
	return render(request, "friends/profile.html")
>>>>>>> ce0f850f09e09352cdfd8f27529f5cc43a565d3b
