(function() {
  var app;

  app = angular.module('crms.app.offer', []);

  app.controller('AppController', [
    '$scope', '$http', function($scope, $http) {
      $scope.offers = [];
      return $http.get('/api/offers').then(function(result) {
        return angular.forEach(result.data, function(item) {
          return $scope.cars.push(item);
        });
      });
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('crms.app.index', []);

  app.controller('AppController', [
    '$scope', '$http', function($scope, $http) {
      $scope.cars = [];
      return $http.get('/api/offers').then(function(result) {
        return angular.forEach(result.data, function(item) {
          return $scope.cars.push(item["car"]);
        });
      });
    }
  ]);

}).call(this);
