//Angular code
(function (){

	angular.module('projectApp').controller("SessionController", ['$http','$scope', '$window', '$cookies', '$location', '$window', '$filter', 'accessService', function ($http, $scope, $window, $cookies, $location, $window, $filter, accessService){

		
	}]);

	/*
	* @name 			projectApp.optionsTemplate.directive
	* @description 		This method execute the optionsTemplate directive and show the template in web page
	* @date 			07/02/2017
	* @author 			Alba Gómez Segura 
	* @version			1.0
	* @params 			none
	* @return 			none
	*/
	angular.module("projectApp").directive("optionsTemplate", function () {
		return {
			restrict: 'E',
			templateUrl:"templates/options-template.html",
			controller:function(){

			},
			controllerAs: 'optionsTemplate'
		};
	});

})();
