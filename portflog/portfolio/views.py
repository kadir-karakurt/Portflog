from django.http import HttpResponse
from django.shortcuts import render
from .models import Project, UserProfile


# Create your views here.


def home(request):
    return render(request, 'portfolio/portfolio.html')

def about(request):
    user_profile = UserProfile.objects.first()
    return render(request, 'portfolio/partials/_about.html', {'user_profile': user_profile})

def profile(request):
    return HttpResponse('<h2>User Profile</h2>')

def portfolio(request):
    projects = Project.objects.all()
    user_profile = UserProfile.objects.first()
    return render(request, 'portfolio/portfolio.html', {'projects': projects, 'user_profile': user_profile})