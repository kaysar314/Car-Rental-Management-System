(function() {
  var app;

  app = angular.module('crms.app.account', []);

  app.controller('AppController', [
  '$scope', '$http', function($scope, $http) {
    $scope.owner;
    var url='/api/users/'+document.getElementById("idd").value;
    $http.get(url).then(function(result) {
        $scope.owner = result.data;
      });
    }
  ]);

}).call(this);

(function() {
  var app;

  app = angular.module('crms.app.index', []);

  app.controller('AppController', [
    '$scope', '$http', function($scope, $http) {
      $scope.offers = [];
      $scope.offer;
      $scope.user;
      $http.get('/api/offers').then(function(result) {
        return angular.forEach(result.data, function(item) {
          return $scope.offers.push(item);
        });
      });
      $scope.onSelect=function(offer){
        $scope.offer = offer;
        $scope.visible = !$scope.visible;
        $scope.visibleuser = false;
      }
      $scope.onSelectuser=function(){
        $scope.visibleuser = !$scope.visibleuser;
      }
    }
  ])
}).call(this);
