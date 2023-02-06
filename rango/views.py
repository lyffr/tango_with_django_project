from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    views_str = "<a href='http://127.0.0.1:8000/rango/about/'>http://127.0.0.1:8000/rango/about/</a>"
    return HttpResponse("Rango says hey there partner!"+views_str)
def about(request):
    views_str = "<a href='http://127.0.0.1:8000/rango/'>http://127.0.0.1:8000/rango/</a>"
    return HttpResponse("Rango says here is the about page "+views_str)