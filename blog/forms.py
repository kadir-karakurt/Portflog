from django import forms
from .models import Blog

# Defines a form for the Blog model. (Blog modeline ait formu tanımlar.)
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'image', 'description', 'is_active', 'is_home', 'categories']