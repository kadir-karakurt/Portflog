from django.contrib import admin
from .models import Project, UserProfile

admin.site.register(UserProfile)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'title')