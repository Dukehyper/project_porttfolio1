# portfolio/models.py

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    about_project = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    upload = models.ImageField(upload_to ='uploads/') 
    
    def __str__(self):
        return self.title
    