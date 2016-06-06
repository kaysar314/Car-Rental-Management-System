(function() {
  var app;

  app = angular.module('crms.app.account', []);

  app.controller('AppController', [
  '$scope', '$http', function($scope, $http) {
    $scope.owner;
    $scope.own;
    var ur = ''
    var host = 'http://'+window.location.host+'/api/';
    var url=host+'users/'+document.getElementById("idd").value;
    $http.get(url).then(function(result) {
      $scope.owner = result.data;
      ur = result.data.profile;
      if($scope.owner.profile){
        $http.get($scope.owner.profile).then(function(result) {
          $scope.owner.profile = result.data;
        });
      }
    });
    $scope.editthis=function(){
      $scope.edit = !$scope.edit;
    }
    $scope.submit=function(){
      $scope.owner.profile.owner = url;
      $http({ method: 'PUT',url: ur,data: $scope.owner.profile,}).then(function successCallback(response){
        $scope.success = {'SUCCESS':'Edit Profile success.'};
          $scope.error = !$scope.error;
        }, function errorCallback(rejection){
        $scope.errors = rejection.data;
          $scope.error = !$scope.error;
        });
    }
  }
  ]);
}).call(this);

// (function() {
//   var app;

//   app = angular.module('crms.app.index', []);

//   app.controller('AppController', [
//     '$scope', '$http', function($scope, $http) {
//       $scope.offers = [];
//       $scope.offer;
//       $scope.user;
//       $http.get('/api/offers').then(function(result) {
//         return angular.forEach(result.data, function(item) {
//           return $scope.offers.push(item);
//         });
//       });
//       $scope.onSelect=function(offer){
//         $scope.offer = offer;
//         $scope.visible = !$scope.visible;
//         $scope.visibleuser = false;
//       }
//       $scope.onSelectuser=function(){
//         $scope.visibleuser = !$scope.visibleuser;
//       }
//     }
//   ])
// }).call(this);

(function() {
  var app;

  app = angular.module('crms.app.index', ['crms.api']);

  app.controller('AppController', [
    '$scope', 'Offer', 'Car' ,'$http', 'Deal',function($scope, Offer, Car,$http,Deal) {
      $scope.visible = true;
      $scope.offers = Offer.query();
      $scope.cars = {};
      $scope.offer;
      $scope.user;
      var host = 'http://'+window.location.host+'/api/';
      $scope.onSelect=function(offer){
        $scope.offer = offer;
        $scope.visible = !$scope.visible;
        $scope.visibleuser = false;
        $scope.deal = new Deal();
        $scope.deal.is_accept = false;
        $scope.deal.offer = host+'offers/'+String($scope.offer.id)+'/';
        $scope.deal.tenant = host+'users/'+document.getElementById("idd").value+'/';
        $scope.rent=function(){
          // alert($scope.deal.offer+"\n"+$scope.deal.tenant+"\n"+$scope.deal.fetch_date+'\n'+$scope.deal.return_date);
          $scope.deal.fetch_date = $scope.deal.fetch_date+'T12:00:00Z';
          $scope.deal.return_date = $scope.deal.return_date+'T12:00:00Z';
          $http.post('/api/deals/', $scope.deal).then(function successCallback(response){
            $scope.success = {'SUCCESS':'You just register a deal,please wait the owner to accept.'};
            $scope.error = !$scope.error;
          }, function errorCallback(rejection){
            $scope.errors = rejection.data;
            $scope.error = !$scope.error;
          });
        }
      }
      $scope.onSelectuser=function(){
        $scope.visibleuser = !$scope.visibleuser;
      }
      $scope.offers.$promise.then(function(results) {
        angular.forEach(results, function(offer) {
          $http.get(offer.car).then(function(result) {
            $scope.cars[offer.car] = result.data;
          });
        });
      });
      $scope.rentit=function(){

      }
    }
  ]);
}).call(this);

(function() {
  var app;

  app = angular.module('crms.api', ['ngResource']);

  app.factory('Offer', [
    '$resource', function($resource) {
      return $resource('/api/offers/:id', {id: '@id'}, {query: {method:'GET',isArray:true}});
    }
  ]);

  app.factory('Car', [
    '$resource', function($resource) {
      return $resource('/api/cars/:id')
    }
  ]);

  app.factory('User', [
    '$resource', function($resource) {
      return $resource('/api/users/:id', {
        id: '@id'
      });
    }
  ]);

  app.factory('Profile', [
    '$resource', function($resource) {
      return $resource('/api/users/:username/posts/:id');
    }
  ]);

  app.factory('Deal', [
    '$resource', function($resource) {
      return $resource('/api/posts/:post_id/photos/:id');
    }
  ]);

}).call(this);