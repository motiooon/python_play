angular.module('myapp')
  .controller('HomeController', ['$scope', '$http', '$sanitize', function ($scope, $http, $sanitize) {


        $http({method: 'GET', url: '/people'}).
            success(function(data, status, headers, config) {
              $scope.people = data.reverse();
            }).
            error(function(data, status, headers, config) {
              // called asynchronously if an error occurs
              // or server returns response with an error status.
            });




  }]);
