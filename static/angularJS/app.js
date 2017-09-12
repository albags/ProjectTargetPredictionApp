// jQuery code
$(document).ready(function () {

});

// Angular code
(function(){
    var projectApp = angular.module('projectApp', ['ng-currency', 'ui.bootstrap', 'ngCookies', 'angularUtils.directives.dirPagination']);

    /*
	* @name         accessService
	* @description  This method defines the access to the server for all the controllers
	* @date         15/03/2017
	* @author       Alba Gomez Segura
	* @version      1.2
	* @params       none
	* @return       none
	*/
	projectApp.factory('accessService', function($http, $log, $q) {
		return {
			getData: function(url, async, method, data) {
				var deferred = $q.defer();
				$http({
					url: url,
					method: method,
					asyn: async,
					data: data
				})
				.success(function(response, status, headers, config)  {
					deferred.resolve(response);
				})
				.error(function(msg, code) {
					deferred.reject(msg);
					$log.error(msg, code);
					alert("There has been an error in the server, try later. appController");
				});
				return deferred.promise;
			}
		}
	});
})();
