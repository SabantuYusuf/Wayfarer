from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.


def home(request):
	return HttpResponse('<h1>Wayfarer Home Page</h1>')

def about(request):
	return render(request, 'about.html')