from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h1>Hi</h1>")
def greet(request, name):
    return HttpResponse(f"<h1>reg,{name.title()}")