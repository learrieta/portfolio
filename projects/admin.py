from django.contrib import admin

# Register your models here.
from projects.models import Project
from .models import Tag, Feature_Project, Development_Enviroment


admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Feature_Project)
admin.site.register(Development_Enviroment)