from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
import random

# Create your views here.

def profile(request):
	return render(request, "friends/profile.html")

def login(request):
	return render(request, "friends/login.html")

def register(request):
	return render(request, "friends/register.html")

def add_user(request):
	return redirect(reverse("friends:login"))

def roll(request):
	return render(request, "friends/roll.html")

def dice(request):
	if request.method == "POST":
		if "coins" not in request.session:
			request.session["coins"] = 0
		a = random.randrange(1, 6)
		request.session["coins"] += a 
		return redirect(reverse("friends:roll"))