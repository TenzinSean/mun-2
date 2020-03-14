from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render

def HomePage(request):
	return render(request, "home/home.html")
	
