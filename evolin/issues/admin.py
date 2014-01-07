from django.contrib import admin

from evolin.issues.models import Issue, IssueState


class IssueAdmin(admin.ModelAdmin):
    list_display = ['number', 'title', 'project', 'state']


admin.site.register(Issue, IssueAdmin)
admin.site.register(IssueState)
