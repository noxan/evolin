from django.db import models
from django.conf import settings


class Project(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    @property
    def full_name(self):
        return '%s/%s' % (self.owner, self.name)

    def __str__(self):
        return self.full_name
