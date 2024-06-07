from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from blog.models import Blog, Category
from django.db.models import Q
from django.db import models
from .forms import BlogForm
from django.contrib.auth.decorators import login_required

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
    query = request.GET.get('q')
    if query:
        blogs = Blog.objects.filter(
            models.Q(title__icontains=query) | models.Q(description__icontains=query)
        )
    else:
        blogs = Blog.objects.none()

    context = {
        "blogs": blogs,
        "categories": Category.objects.all(),
        "query": query
    }
    return render(request, "blog/search_results.html", context)

'''def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogForm()
    
    return render(request, 'blog/add_blog.html', {'form': form, 'categories': Category.objects.all()})
'''
@login_required # Disallow adding a blog without admin login
def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('index')
    else:
        form = BlogForm()
    
    return render(request, 'blog/add_blog.html', {'form': form, 'categories': Category.objects.all()})
def contact(request):
    return render(request, 'blog/contact.html', {'categories': Category.objects.all()})