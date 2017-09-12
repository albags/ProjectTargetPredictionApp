// JQuery code
$( document ).ready(function() {
	try {
		// Get the modal
		var modal = document.getElementById('myModalTarget');

		// Get the button that opens the modal
		var btn = document.getElementById("confirmButtonTarget");

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

		if (this.targetAction == 1) {
		    modal.style.display = "none";
		}
	} catch (err) {

	}

});

// Angular code
(function (){
	angular.module('projectApp').controller("TargetController", ['$http','$scope', '$window', '$cookies', '$location', '$window', '$filter', 'accessService', function ($http, $scope, $window, $cookies, $location, $window, $filter, accessService){

		// Scope variables for smiles management
		$scope.smilesArray = [];
		$scope.compoundNameList = ["Acetylcysteine", "Caffeine", "Chlormezanone", "Tertosterone"];
		$scope.compoundSmilesList = ["CC(=O)N[C@@H](CS)C(=O)O", "CN1C(=O)N(C)c2ncn(C)c2C1=O", "CN1C(c2ccc(Cl)cc2)S(=O)(=O)CCC1=O", "C[C@]12CC[C@H]3[C@@H](CCC4=CC(=O)CC[C@]34C)[C@@H]1CC[C@@H]2O"];

		//Scope variables for targets
		$scope.targetAction = 0;
		$scope.targetId = 0;
		$scope.compoundTarget;
		$scope.targetsArray = new Array();
		$scope.filteredData = new Array();
		$scope.errorMessage;

		//Pagination variables
		$scope.pageSize = 10;
		$scope.currentPage = 1;

		$scope.$watch("gene_name+target_class",function () {
			$scope.filteredData = $filter('filter')($scope.targetsArray,{gene_name:$scope.gene_name, target_class:$scope.target_class});
		});

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
			$scope.compoundTarget.setSmile('');
			$("#smileCompound").removeClass("ng-invalid");
			$scope.targetManagement.$invalid = true;
		}

		/*
		* @name         initializeSmileObject
		* @description  This method initialize smile object to do change function
		* @date         15/03/2017
		* @author       Alba Gomez Segura
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
		* @name         initTargetsForm
		* @description  This method calls to the method that creates all the examples of smiles objects and initialize the smile molecule object
		* @date         02/05/2017
		* @author       Alba Gómez Segura
		* @version      1.0
		* @params       none
		* @return       none
		*/
		this.initTargetsForm = function () {
			$scope.initializeSmileObject();
			$scope.compoundTarget = new MoleculeTargetForm();
			$scope.compoundTarget.setId($scope.targetId);
		}

		/*
		* @name         sendCompoundTargetInfo
		* @description  This method sends the molecule introduced to the server through ajax to get the information required. Shows the information to the user
		* @date         02/05/2017
		* @author       Alba Gómez Segura
		* @version      1.0
		* @params       none
		* @return       none
		*/
		this.sendCompoundTargetInfo = function () {
			$scope.clickAbort = false;
			// Copy
			$scope.compoundTarget = angular.copy($scope.compoundTarget);

			// Server conenction to verify targets's data
			var promise = accessService.getData( "/targetResults", true, "POST", {action:10000,compound:$scope.compoundTarget} );

			promise.then(function (response) {
				if(response.status === true) {
					console.log(response);
					if (response.results.length == 0) {
						$scope.errorMessage = 'No targets found.';
					} else {
						for (var i = 0; i < response.results.length; i++) {
							var molecule = new MoleculeTargetResult();
							molecule.construct(i, response.results[i]['target'], response.results[i]['gene_name'], response.results[i]['uniprot_id'], response.results[i]['chembl_id'], response.results[i]['target_class']);
							$scope.targetsArray.push(molecule);
						};
						var data = [{
							values: response.values,
							labels: response.labels,
							type: 'pie'
						}];
						var layout = {
						  	height: 380,
						  	width: 700
						};
						Plotly.newPlot('myTargetsPlot', data, layout);
					}
					if ($scope.clickAbort == false) {
						$scope.targetAction = 1;
					}
					// $scope.targetAction = 1;
					d = new Date();
					$("#imgTargetQuery").attr("src", "static/images/queryMolecule/queryMolecule.png?"+d.getTime());
					$scope.filteredData = $scope.targetsArray;
				} else {
					if(angular.isArray(response.results)) {
						alert("Error with response status");
					}
					else {alert("There has been an error in the server, try later. sendCompoundTargetInfo in TargetController");}
				}
			});
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
			if ($scope.compoundTarget.getSmile().trim().match(/^([^J][0-9BCOHNSOPrIFla@+\-\[\]\(\)\\\/%=#$]{6,})$/ig) == null) {
				$("#smileCompound").removeClass("ng-valid").addClass("ng-invalid");
				$scope.targetManagement.$invalid = true;
			} else {
				$("#smileCompound").removeClass("ng-invalid").addClass("ng-valid");
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
			$("#smileCompound").addClass("ng-valid ng-dirty");
			$scope.compoundTarget.setSmile(smile);
		}

	}]);
	
	// directive

})();