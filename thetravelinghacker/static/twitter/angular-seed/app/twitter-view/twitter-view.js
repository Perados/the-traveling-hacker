'use strict';

angular.module('myApp.twitter', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {
    templateUrl: '/static/twitter/angular-seed/app/twitter-view/twitter-view.html',
    controller: 'TwitterCtrl'
  });
}])

.controller('TwitterCtrl', ['$scope', '$http', function($scope, $http) {
  $scope.handle = ''
  $scope.loading = ''
  $scope.appLaunched = false

  $scope.go = function(handle){
    $scope.loading = 'This handle is being loaded: ' + handle
    $http.get('/api/twitter-users/'+handle+'/').success(function(data) {
      $scope.data = data

      $scope.loading = ''
      $scope.appLaunched = true
    })
  }
}]);