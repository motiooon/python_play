angular.module('myapp')
  .controller('UploadController', ['$scope', '$http', '$sanitize', '$fileUploader', function ($scope, $http, $sanitize, $fileUploader) {

        // create a uploader with options
        var uploader = $scope.uploader = $fileUploader.create({
            scope: $scope,                          // to automatically update the html. Default: $rootScope
            url: '/upload',
            formData: [
                { key: 'value' }
            ]
        });

        $scope.upload = function (){
            uploader.uploadItem($scope.item);
        };

        uploader.bind('afteraddingfile', function (event, item) {
            console.info('After adding a file', item);
            $scope.item = item;
        });

         uploader.bind('success', function (event, xhr, item, response) {
            console.info('Success', xhr, item, response);
        });

  }]);
