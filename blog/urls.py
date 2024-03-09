from django.urls import path
from . import views

# http://127.0.0.1:8000/            => homepage
# http://127.0.0.1:8000/index       => homepage
# http://127.0.0.1:8000/blogs       => blogs
# http://127.0.0.1:8000/blogs/3     => blogs-details
# http://127.0.0.1:8000/blogs/      => blogs-details


urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index),
    path('blogs',views.blogs, name='blogs'),
    path('post', views.post,name='post'),
    path('blogs/<slug:slug>', views.details, name="blog_details"),
]