'use strict';

var customerApp = angular.module('customerApp', []);

customerApp.config(['$httpProvider', function ($httpProvider) {
	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);



