from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import SessionAuthentication

from evolin.projects.models import Project


class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projects'
        authorization = DjangoAuthorization()
        authentication = SessionAuthentication()

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user=request.user)
