from django.contrib import admin
from .models import Project, UserProfile

admin.site.register(UserProfile)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'title')
    
    

# Configures the admin panel. (Admin paneli yapılandırmasını yapar.)
# Manages Project and UserProfile models in the admin panel. (Proje ve Kullanıcı Profili modellerini admin panelinde yönetir.)