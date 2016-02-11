'use strict';

angular.module('myApp.twitter', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {
    templateUrl: '/static/twitter/angular-seed/app/twitter-view/twitter-view.html',
    controller: 'TwitterCtrl'
  });
}])

.controller('TwitterCtrl', ['$scope', '$http', function($scope, $http) {
  $scope.handle = '';
  $scope.loading = false;
  $scope.appLaunched = false;

  $scope.sortType = '-date';
  $scope.hide = false;

  $scope.noPhotoChecked = false;
  $scope.moreThanRetweetsChecked = false;
  $scope.lessThanRetweetsChecked = false;
  $scope.beforeDateChecked = false;
  $scope.afterDateChecked = false;

  $scope.toggleHideTweets = function() {
    $scope.hide = !$scope.hide;
    setTimeout(
       // Yes... This is a despicable hack to fix Twitter's widget.
       // And it works like a charm...
      function() {
        $scope.hide= !$scope.hide;
      }, 10);

  };

  $scope.go = function(handle){
    $scope.loading = true;
    $scope.handle = handle;
    $http.get('/api/twitter-users/'+handle+'/').success(function(data) {
      $scope.data = data;
      $scope.loading = false;
      $scope.appLaunched = true;
    })
    .error(function (data, status) {
      $scope.data = data;
      $scope.loading = false
    })
  };

  $scope.customFilter = function(tweet) {
    var returnTweet = true;
    if ($scope.noPhotoChecked) {
      if (tweet.photo == "") {
        returnTweet = false;
      }
    }

    if ($scope.moreThanRetweetsChecked) {
      if (tweet.retweets_count > $scope.moreThanRetweets) {
        returnTweet = false;
      }
    }

    if ($scope.lessThanRetweetsChecked) {
      if (tweet.retweets_count < $scope.lessThanRetweets) {
        returnTweet = false;
      }

    }

    if ($scope.beforeDateChecked) {
      if (Date.parse(tweet.date) < Date.parse($scope.beforeDate)) {
        returnTweet = false;
      }
    }
    if ($scope.afterDateChecked) {
      if (Date.parse(tweet.date) > Date.parse($scope.afterDate)) {
        returnTweet = false;
      }
    }

    if (returnTweet) {
      return tweet;
    }
  };
  $scope.maxDate = new Date();

  $scope.open1 = function() {
    $scope.popup1.opened = true;
  };

  $scope.open2 = function() {
        $scope.popup2.opened = true;
  };

  $scope.dateOptions = {
    formatYear: 'yy',
    startingDay: 1
  };

  $scope.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
  $scope.format = $scope.formats[0];
  $scope.altInputFormats = ['M!/d!/yyyy'];

  $scope.popup1 = {
    opened: false
  };

  $scope.popup2 = {
    opened: false
  };

}]);
