// jQuery code
$( document ).ready(function() {
	try {
		var modalForm = document.getElementById('myModalDrug');

		// Get the button that opens the modal
		var btn = document.getElementById("confirmButtonDrug");

		// When the user clicks on the button, open the modal 
		btn.onclick = function() {
			modalForm.style.display = "block";
		}

		// Get the <span> element that closes the modal
		var span = document.getElementsByClassName("close")[0];

		// When the user clicks on <span> (x), close the modal
		span.onclick = function() {
		    modal.style.display = "none";
		}

		if (this.drugAction == 1) {
			modalForm.style.display = "none";
		}
	} catch (err) {
		
	}

	try {
		// Get the modal
		var modal = document.getElementById('myModal');

		// Get the image and insert it inside the modal - use its "alt" text as a caption
		var img = document.getElementById('imgDrugQuery');
		var modalImg = document.getElementById("img01");
		var captionText = document.getElementById("caption");
		img.onclick = function(){
			modal.style.display = "block";
			modalImg.src = this.src;
			captionText.innerHTML = this.alt;
		}

		// When the user clicks anywhere outside of the modal, close it
		window.onclick = function(event) {
			if (event.target == modal) {
				modal.style.display = "none";
			}
		}
	} catch (err) {
		
	}
});

// Angular code
(function (){
	angular.module('projectApp').controller("DrugController", ['$http','$scope', '$window', '$cookies', '$location', '$window', '$filter', 'accessService', function ($http, $scope, $window, $cookies, $location, $window, $filter, accessService){

		//Scope variables for targets
		$scope.drugAction = 0;
		$scope.drugId = 0;
		$scope.compoundDrug = {};
		$scope.compoundResult = {};
		$scope.errorMessage;

		/*
		* @name         initDrugForm
		* @description  This method initialize the drug query
		* @date         02/05/2017
		* @author       Alba Gómez Segura
		* @version      1.0
		* @params       none
		* @return       none
		*/
		this.initDrugForm = function () {
			$scope.compoundDrug = new MoleculeDrugForm();
			$scope.compoundDrug.setId($scope.drugId);
		}

		/*
		* @name         checkDbId
		* @description  This method checks if the smile written by the user it is correct
		* @date         02/05/2017
		* @author       Alba Gómez Segura
		* @version      1.0
		* @params       none
		* @return       none
		*/
		this.checkDbId = function () {
			try {
				if ($scope.compoundDrug.getMoleculeId().trim().match(/^(DB[0-9]{5})$/ig) == null) {
					$("#dbCompoundDrug").removeClass("ng-valid").addClass("ng-invalid");
					$scope.drugManagement.$invalid = true;
				} else {
					$("#dbCompoundDrug").removeClass("ng-invalid").addClass("ng-valid");
					$scope.drugManagement.$invalid = false;
				}
			} catch (e) {
				$("#dbCompoundDrug").removeClass("ng-valid").addClass("ng-invalid");
			}
		}

		/*
		* @name         sendCompoundDrugInfo
		* @description  This method sends the drug introduced to the server through ajax to get the information required. Shows the information to the user
		* @date         02/05/2017
		* @author       Alba Gómez Segura
		* @version      1.0
		* @params       none
		* @return       none
		*/
		this.sendCompoundDrugInfo = function () {
			$scope.clickAbort = false;
			// Copy
			$scope.compoundDrug = angular.copy($scope.compoundDrug);

			// Server conenction to verify targets's data
			var promise = accessService.getData( "/drugResults", true, "POST", {action:10000,compound:$scope.compoundDrug} );

			promise.then(function (response) {
				if(response.status === true) {
					var molecule = new MoleculeDrugResult();
					molecule.construct(0, response.results['name'], response.results['description'], response.results['drugbank-id'], response.results['groups'], response.results['identifier'], response.results['indication'], response.results['mechanism-of-action'], response.results['metabolism'], response.results['protein-binding'], response.results['route-of-elimination'], response.results['routes'], response.results['smile'], response.results['synonyms'], response.results['toxicity'], response.results['type']);
					$scope.compoundResult = molecule;
					console.log(response);
					if ($scope.clickAbort == false) {
						$scope.drugAction = 1;
					}
					if (!response.results['name']) {
						$scope.errorMessage = 'Molecule not found.';
					}
					d = new Date();
					$("#imgDrugQuery").attr("src", "static/images/queryMolecule/queryMolecule.png?"+d.getTime());
				} else {
					if(angular.isArray(response.results)) {
						alert("Error with response status");
					}
					else {alert("There has been an error in the server, try later. sendCompoundDrugInfo in DrugController");}
				}
			});
		}

	}]);
	
	// directive

})();