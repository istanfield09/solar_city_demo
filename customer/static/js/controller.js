'use strict';


customerApp.controller('CustomerFormController',

		function ($scope, $http) {
				$scope.processForm = function (customer) {

					var request = $http({
						method: "POST",
						url: "",
						data: { customer }
						}).success(function (data) {
							console.log("Success!");
					});

				}
		}
);
