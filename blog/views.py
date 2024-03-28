from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from blog.models import Blog, Category

# Create your views here. 

def index(request):
    # Arama terimi (q) var mı kontrol ediyoruz
    if 'q' in request.GET:
        q = request.GET.get('q')
        # Başlıkta arama yapıp ilgili blogları filtreliyoruz
        blogs = Blog.objects.filter(title__icontains=q)
        context = {
            "blogs": blogs,
            "categories": Category.objects.all()
        }
        return render(request, "blog/search_results.html", context)
    else:
        # Arama terimi yoksa tüm blogları ve kategorileri getiriyoruz
        context = {
            "blogs": Blog.objects.filter(is_active=True, is_home=True),
            "categories": Category.objects.all()
        }
        return render(request, "blog/index.html", context)


def details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/details.html", {
        "blog": blog,
        "categories": Category.objects.all()
    })

def post(request):
    return render(request, "blog/post.html")


def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/index.html", context)

def search_blogs(request):
    # Arama terimi (q) var mı kontrol ediyoruz
    if 'q' in request.GET:
        q = request.GET.get('q')
        # Başlıkta arama yapıp ilgili blogları filtreliyoruz
        blogs = Blog.objects.filter(title__icontains=q,description__icontains=q)
        context = {
            "blogs": blogs,
            "categories": Category.objects.all()
        }
        return render(request, "blog/search.html", context)
    else:
        # Arama terimi yoksa tüm blogları ve kategorileri getiriyoruz
        context = {
            "blogs": Blog.objects.filter(is_active=True, is_home=True),
            "categories": Category.objects.all()
        }
        return render(request, "blog/index.html", context)