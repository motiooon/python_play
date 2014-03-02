angular.module('myapp')
  .controller('CreateController', ['$scope', '$http', '$location', function ($scope, $http, $location) {


        // setup editor options
            $scope.editorOptions = {
                language: 'en'
            };

            $scope.save = function() {
                $http.post('/people', {
                    content: $scope.text
                }).success(function() {
                    $location.path( "/" );
                });
            }

  }]);
