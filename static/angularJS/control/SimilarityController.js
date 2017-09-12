// JQuery code
$( document ).ready(function() {
	try {
		// Get the modal
		var modal = document.getElementById('myModalSimil');

		// Get the button that opens the modal
		var btn = document.getElementById("confirmButtonSimilarity");

		// When the user clicks on the button, open the modal 
		btn.onclick = function() {
		    modal.style.display = "block";
		}

		// Get the <span> element that closes the modal
		var span = document.getElementsByClassName("close")[0];

		// When the user clicks on <span> (x), close the modal
		span.onclick = function() {
		    modal.style.display = "none";
		}

		if (this.similarityAction == 1) {
		    modal.style.display = "none";
		}
	} catch (err) {

	}

});

// Angular code
(function (){
	angular.module('projectApp').controller("SimilarityController", ['$http','$scope', '$window', '$cookies','accessService', function ($http, $scope, $window, $cookies, accessService){

		// Scope variables for smiles management
		$scope.smilesArray = [];
		$scope.compoundNameList = ["Diazepam", "Lidocaine", "Naproxen", "Amoxicillin"];
		$scope.compoundSmilesList = ["CN1C(=O)CN=C(c2ccccc2)c3cc(Cl)ccc13", "CCN(CC)CC(=O)Nc1c(C)cccc1C", "COc1ccc2cc(ccc2c1)[C@H](C)C(=O)O", "CC1(C)S[C@@H]2[C@H](NC(=O)[C@H](N)c3ccc(O)cc3)C(=O)N2[C@H]1C(=O)O"];

		//Scope variables for similarities
		$scope.similarityAction = 0;
		$scope.similarityId = 0;
		$scope.compoundSimilarity = {};
		$scope.similarityArray = new Array();
		$scope.errorMessage;

		/*
		* @name         clear
		* @description  This method cleans the smile input
		* @date         02/05/2017
		* @author       Alba Gómez Segura
		* @version      1.0
		* @params       none
		* @return       none
		*/
		$scope.clear = function () {
			$scope.compoundSimilarity.setSmile('');
			$("#smileCompoundSim").removeClass("ng-invalid");
			$scope.similarityManagement.$invalid = true;
		}

		/*
		* @name         initializeSmileObject
		* @description  This method initializes smile object to do change function
		* @date         02/05/2017
		* @author       Alba Gómez Segura
		* @version      1.2
		* @params       none
		* @return       none
		*/
		$scope.initializeSmileObject = function() {
			$scope.smilesArray = [];
			var smileExemple = {};
			for (var i=0; i<$scope.compoundNameList.length; i++) {
				smileExemple = new Smile();
				smileExemple.construct(i, $scope.compoundNameList[i], $scope.compoundSmilesList[i]);
				$scope.smilesArray.push(smileExemple);
			}
		}

		/*
		* @name         initSimilarityForm
		* @description  This method calls to the method that creates all the examples of smiles objects and initialize the smile molecule object
		* @date         02/05/2017
		* @author       Alba Gómez Segura
		* @version      1.0
		* @params       none
		* @return       none
		*/
		this.initSimilarityForm = function () {
			$scope.initializeSmileObject();
			$scope.compoundSimilarity = new MoleculeSimilarityForm();
			$scope.compoundSimilarity.setId($scope.similarityId);
		}

		/*
		* @name         checkSmile
		* @description  This method compare the string given with the smile official pattern
		* @date         15/03/2017
		* @author       Alba Gomez Segura
		* @version      1.2
		* @params       none
		* @return       none
		*/
		this.checkSmile = function () {
			if ($scope.compoundSimilarity.getSmile().trim().match(/^([^J][0-9BCOHNSOPrIFla@+\-\[\]\(\)\\\/%=#$]{6,})$/ig) == null) {
				$("#smileCompoundSim").removeClass("ng-valid").addClass("ng-invalid");
				$scope.similarityManagement.$invalid = true;
			} else {
				$("#smileCompoundSim").removeClass("ng-invalid").addClass("ng-valid");
			}
		}

		/*
		* @name         getSmileExemple
		* @description  This method set the smile in input field 
		* @date         15/03/2017
		* @author       Alba Gomez Segura
		* @version      1.2
		* @params       Smile string to set
		* @return       none
		*/
		this.getSmileExemple = function (smile) {
			$("#smileCompoundSim").addClass("ng-valid ng-dirty");
			$scope.compoundSimilarity.setSmile(smile);
		}

		/*
		* @name         sendCompoundSimilarityInfo
		* @description  This method sends the molecule introduced to the server through ajax to get the information required. Shows the information to the user
		* @date         02/05/2017
		* @author       Alba Gómez Segura
		* @version      1.0
		* @params       none
		* @return       none
		*/
		this.sendCompoundSimilarityInfo = function () {
			$scope.clickAbort = false;
			// Copy
			$scope.compoundSimilarity = angular.copy($scope.compoundSimilarity);

			// Server conenction to verify targets's data
			var promise = accessService.getData( "/similarityResults", true, "POST", {action:10000,compound:$scope.compoundSimilarity} );

			promise.then(function (response) {
				if(response.status === true) {
					for (var i = 0; i < response.results.length; i++) {
						var molecule = new MoleculeSimilarityResult();
						molecule.construct(i, response.results[i]['smile'], response.results[i]['chembl_id'], response.results[i]['similarity']);
						$scope.similarityArray.push(molecule);
					};
					console.log(response);
					if ($scope.clickAbort == false) {
						$scope.similarityAction = 1;
					}
					if (response.results.length == 0) {
						$scope.errorMessage = 'No similar molecules found.';
					}
					d = new Date();
					$("#imgSimilarityQuery").attr("src", "static/images/queryMolecule/queryMolecule.png?"+d.getTime());
				} else {
					if(angular.isArray(response.results)) {
						alert("Error with response status");
					}
					else {alert("There has been an error in the server, try later. sendCompoundSimilarityInfo in SimilarityController");}
				}
			});
		}

		$scope.abortConnection  = function () {
			// promise.abort();
			var canceler = $q.defer();
			canceler.resolve();
		}		


	}]);
	
	// directive

})();