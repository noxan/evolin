@services = angular.module 'evolinServices', ['ngResource']

tastypieTransformer = ($http) ->
  return $http.defaults.transformResponse.concat([
    (data, headersGetter) ->
      result = data.objects
      result.meta = data.meta
      return result
  ])


@services.factory 'Issue', ['$http', '$resource', ($http, $resource) ->
  $resource '/api/v1/issues/:issueId/', {},
    query:
      cache : true
      method: 'GET'
      transformResponse: tastypieTransformer($http)
      isArray: true
      params:
        issueId: ''
]


@app = angular.module 'evolinApp', [
  'ngRoute'
  'evolinServices'
]

@app.config ['$routeProvider', ($routeProvider) ->
  $routeProvider.when('/issues',
    templateUrl: '/static/partials/issues/issue_list.html'
    controller: 'IssueListCtrl'
  ).when('/issues/:issueId',
    templateUrl: '/static/partials/issues/issue_detail.html'
    controller: 'IssueDetailCtrl'
  ).otherwise(
    redirectTo: '/issues'
  )
]

@app.controller 'IssueListCtrl', ['$scope', 'Issue', ($scope, Issue) ->
  $scope.issues = Issue.query()
]

@app.controller 'IssueDetailCtrl', ['$scope', '$routeParams', 'Issue', ($scope, $routeParams, Issue) ->
  $scope.issues = Issue.get({issueId: $routeParams.issueId}, (issue) ->
    $scope.issue = issue
  )
]
