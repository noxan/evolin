from django.db import models

from evolin.projects.models import Project


class IssueState(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.name


class Issue(models.Model):
    number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True, default='')
    state = models.ForeignKey(IssueState)
    project = models.ForeignKey(Project)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '#%d - %s' % (self.number, self.title)

    class Meta:
        ordering = ['project', 'number']
        unique_together = (('project', 'number'),)
