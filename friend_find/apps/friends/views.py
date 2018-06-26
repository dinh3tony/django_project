from django.shortcuts import render, HttpResponse, redirect

def login(request):
	return render(request, "friends/login.html")
