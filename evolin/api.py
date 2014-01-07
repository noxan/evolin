from tastypie.api import Api

from evolin.issues.api import IssueResource, IssueStateResource


api_v1 = Api(api_name='v1')
api_v1.register(IssueResource())
api_v1.register(IssueStateResource())
