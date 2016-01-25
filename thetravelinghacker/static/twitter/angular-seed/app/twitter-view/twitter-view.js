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
  $scope.loading = false
  $scope.appLaunched = false

  $scope.go = function(handle){
    $scope.loading = true
    $scope.handle = handle
    $http.get('/api/twitter-users/'+handle+'/').success(function(data) {
      $scope.data = data
      $scope.loading = false
      $scope.appLaunched = true
    })
  }
}]);