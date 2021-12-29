from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):       # para hacer unicamente visible en el panel de los campos del modelo que corresponden a: created y updated.
    readonly_fields =  ('created', 'updated')

admin.site.register(Project, ProjectAdmin)    # para habilitar la opcion de gestionar Projectos desde el panel Admin
