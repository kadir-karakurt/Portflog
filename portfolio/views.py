from django.http import HttpResponse
from django.shortcuts import render
from .models import Project, UserProfile



# Returns the homepage (Ana sayfayı döndürür.)
def home(request):
    return render(request, 'portfolio/portfolio.html')

# Returns the about page (Hakkında sayfasını döndürür.)
def about(request):
    user_profile = UserProfile.objects.first()
    return render(request, 'portfolio/partials/_about.html', {'user_profile': user_profile})

# Returns a simple HTML response for the user profile.(Kullanıcı profili için basit bir HTML yanıt döndürür.)
def profile(request):
    return HttpResponse('<h2>User Profile</h2>')

# Lists all projects and the user's profile. (Tüm projeleri ve kullanıcının profilini listeler.)
def portfolio(request):
    projects = Project.objects.all()
    user_profile = UserProfile.objects.first()
    return render(request, 'portfolio/portfolio.html', {'projects': projects, 'user_profile': user_profile})