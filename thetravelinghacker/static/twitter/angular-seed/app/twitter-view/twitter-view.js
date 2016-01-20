'use strict';

angular.module('myApp.twitter', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {
    templateUrl: '/static/twitter/angular-seed/app/twitter-view/twitter-view.html',
    controller: 'TwitterCtrl'
  });
}])

.controller('TwitterCtrl', ['$scope', function($scope) {
  $scope.handle = ''
  $scope.test = ''

  $scope.go = function(handle){
    $scope.test = 'The handle is: ' + handle
  }
}]);