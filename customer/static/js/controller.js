'use strict';


customerApp.controller('CustomerFormController',

		function ($scope, $http) {
				$scope.processForm = function (customer) {
					var request = $http({
						method: "post",
						url: "/index.html",
						data: { "content": "Hooo boy!" }
					});
				}
		}
);
