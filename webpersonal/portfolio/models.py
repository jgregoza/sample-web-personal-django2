from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects")
    link = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created"]    # para ordenar por el mas nuevo
    
    def __str__(self):      # para mostrar el titulo de mis proyectos en el panel Admin
        return self.title