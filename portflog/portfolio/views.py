from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('<h2>Home</h2>')

def posts(request):
    return HttpResponse('<h2>Posts</h2>')

def post(request):
    return HttpResponse('<h2>Post Title</h2>')

def profile(request):
    return HttpResponse('<h2>User Profile</h2>')