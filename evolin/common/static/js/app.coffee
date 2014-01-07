@IssueCtrl = ($scope, $http) ->
  $http.get('/api/v1/issue/').success (data, status, headers, config) ->
    $scope.issues = data.objects
