from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse

# Create your views here.
data = {
    "blogs": [
        {
            "id":1,
            "title": "Komple Web Geliştirme",
            "image": "img-01.jpg",
            "is_active": True,
            "is_home": False,
            "description": "Çok iyi bir kurs"
        },
        {
            "id":2,
            "title": "Python Kursu",
            "image":  "img-02.jpg",
            "is_active": True,
            "is_home": True,
            "description": "Çok iyi bir kurs"
        },
        {
            "id":3,
            "title": "django kursu",
            "image":  "img-03.jpg",
            "is_active": False,
            "is_home": True,
            "description": "Çok iyi bir kurs"
        }
    ]    
    
}


def index(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": data["blogs"]
    }
    return render(request, "blog/blogs.html", context)

def details(request, id):
    # blogs = data["blogs"]
    # selectedBlog = None

    # for blog in blogs:
    #     if blog["id"] == id:
    #         selectedBlog = blog
    blogs = data["blogs"]

    selectedBlog = [blog for blog in blogs if blog["id"]==id][0]

    return render(request, "blog/details.html", {
        "blog": selectedBlog
    })

def post(request):
    return render(request, "blog/post.html")
