from django.contrib import admin
from .models import Contact, Project

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','about_project','created_at')
    search_fields = ('name', 'email')
    
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'description')
    search_fields = ('title', 'url')