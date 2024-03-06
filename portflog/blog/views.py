from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'blog/index.html')

def details(request):
    return HttpResponse ("Blog Detayları")

def post(request):
    return render (request, 'blog/post.html')