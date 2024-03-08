from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField()
    slug = models.SlugField(default="",blank=True,null=False, unique=True, db_index=True)
    
