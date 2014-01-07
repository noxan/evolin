from django.contrib import admin

from evolin.issues.models import Issue


class IssueAdmin(admin.ModelAdmin):
    list_display = ['number', 'title', 'project']


admin.site.register(Issue, IssueAdmin)
