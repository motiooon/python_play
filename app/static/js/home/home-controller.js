angular.module('myapp')
  .controller('HomeController', ['$scope', '$http', function ($scope, $http) {


        $http({method: 'GET', url: '/people'}).
            success(function(data, status, headers, config) {
              $scope.people = data;
            }).
            error(function(data, status, headers, config) {
              // called asynchronously if an error occurs
              // or server returns response with an error status.
            });




  }]);
