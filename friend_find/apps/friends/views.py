from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse

# Create your views here.

def profile(request):
	return render(request, "friends/profile.html")