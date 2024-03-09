from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'portfolio/portfolio.html')

def about(request):
    return HttpResponse('<h2>Posts</h2>')

def profile(request):
    return HttpResponse('<h2>User Profile</h2>')