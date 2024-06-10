from django.urls import path
from . import views
from portfolio.views import portfolio

# http://127.0.0.1:8000/            => homepage
# http://127.0.0.1:8000/index       => homepage
# http://127.0.0.1:8000/blogs       => blogs
# http://127.0.0.1:8000/blogs/3     => blogs-details
# http://127.0.0.1:8000/blogs/      => blogs-details


# Defines URL mappings for the blog application. (Blog uygulaması için URL yönlendirmeleri yapar.)
urlpatterns = [
    path('',views.index,name='index'),
    path('',views.index,name='home'),
    path('index',views.index),
    path('category/<slug:slug>', views.blogs_by_category, name="blogs_by_category"),
    path('post', views.post,name='post'),
    path('details/<slug:slug>', views.details, name="blog_details"),
    path('search', views.search_blogs, name="search_blogs"),
    path('add-blog', views.add_blog, name='add_blog'),
    path('contact', views.contact, name='contact'),
]