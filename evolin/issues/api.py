from tastypie.resources import ModelResource

from evolin.issues.models import Issue, IssueState


class IssueStateResource(ModelResource):
    class Meta:
        queryset = IssueState.objects.all()
        resource_name = 'issuestate'


class IssueResource(ModelResource):
    def dehydrate(self, bundle):
        bundle.data['state'] = bundle.obj.state.name.lower()
        return bundle

    class Meta:
        queryset = Issue.objects.all()
        resource_name = 'issue'
