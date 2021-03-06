// Declare app level module which depends on filters, and services
angular.module('myapp', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date', 'ngCkeditor', 'ngSanitize', 'angularFileUpload'])
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/home.html', 
        controller: 'HomeController'})
      .when('/write', {
        templateUrl: 'views/home/write.html',
        controller: 'CreateController'})
     .when('/upload', {
        templateUrl: 'views/home/upload.html',
        controller: 'UploadController'})
      .otherwise({redirectTo: '/'});
  }]);
