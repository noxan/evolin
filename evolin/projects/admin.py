from django.contrib import admin

from evolin.projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['full_name']


admin.site.register(Project, ProjectAdmin)
