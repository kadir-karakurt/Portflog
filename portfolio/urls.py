from django.urls import path
from . import views
from .views import portfolio

urlpatterns = [
    #path('', views.home, name="home"),
    path('', portfolio, name="portfolio"),
    path('about/', views.about, name="about"),
    path('profile/', views.profile, name="profile"),
    
]

# Defines URL mappings for the portfolio application. (Portfolio uygulaması için URL yönlendirmeleri yapar.)
# URL mappings direct to specific views. (URL'ler, belirli görünümlere (views) yönlendirilir.)

