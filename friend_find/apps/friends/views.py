from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse


def index(request):
	print("*******************************")
	return render(request, "friends/login.html")

def success(request):
	print("This is the login page, it went through")
	return redirect('/wall/')

def wall(request):
	return render(request, "friends/wall.html")

def clear(request):
	return redirect('/')

def page(request):
	return render(request, "friends/edit.html")

def profile(request):
	return render(request, "friends/profile.html")
