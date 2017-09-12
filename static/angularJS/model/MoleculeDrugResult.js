/* @MoleculeDrugResult()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Object molecule results
* @Attributes:
* 		id: id number;
*		name;
* 		description;
*		accessionNumber;
* 		groups;
*		chembl_id;
* 		indication;
*		mechanismOfAction;
* 		metabolism;
*		proteinBinding;
* 		routeOfElimination;
*		routes;
* 		smile;
*		synonyms;
* 		toxicity;
*		type;
* @methods:
* 		construct
* 		set's and get's for each attribute
*		toString: return a string with all object's information
*/

function MoleculeDrugResult () {
	//Attributes declaration
	this.id;
	this.name;
	this.description;
	this.accessionNumber;
	this.groups;
	this.chembl_id;
	this.indication;
	this.mechanismOfAction;
	this.metabolism;
	this.proteinBinding;
	this.routeOfElimination;
	this.routes;
	this.smile;
	this.synonyms;
	this.toxicity;
	this.type;

	//Methods declaration
	this.construct = function (id, name, description, accessionNumber, groups, chembl_id, indication, mechanismOfAction, metabolism, proteinBinding, routeOfElimination, routes, smile, synonyms, toxicity, type) {
		this.setId(id);
		this.setName(name);
		this.setDescription(description);
		this.setAccessionNumber(accessionNumber);
		this.setGroups(groups);
		this.setChemblId(chembl_id);
		this.setIndication(indication);
		this.setMechanismOfAction(mechanismOfAction);
		this.setMetabolism(metabolism);
		this.setProteinBinding(proteinBinding);
		this.setRouteOfElimination(routeOfElimination);
		this.setRoutes(routes);
		this.setSmile(smile);
		this.setSynonyms(synonyms);
		this.setToxicity(toxicity);
		this.setType(type);
		
	}

	this.setId = function (id){this.id=id;}
	this.setName = function (name){this.name=name;}
	this.setDescription = function (description){this.description=description;}
	this.setAccessionNumber = function (accessionNumber){this.accessionNumber=accessionNumber;}
	this.setGroups = function (groups){this.groups=groups;}
	this.setChemblId = function (chembl_id){this.chembl_id=chembl_id;}
	this.setIndication = function (indication){this.indication=indication;}
	this.setMechanismOfAction = function (mechanismOfAction){this.mechanismOfAction=mechanismOfAction;}
	this.setMetabolism = function (metabolism){this.metabolism=metabolism;}
	this.setProteinBinding = function (proteinBinding){this.proteinBinding=proteinBinding;}
	this.setRouteOfElimination = function (routeOfElimination){this.routeOfElimination=routeOfElimination;}
	this.setRoutes = function (routes){this.routes=routes;}
	this.setSmile = function (smile){this.smile=smile;}
	this.setSynonyms = function (synonyms){this.synonyms=synonyms;}
	this.setToxicity = function (toxicity){this.toxicity=toxicity;}
	this.setType = function (type){this.type=type;}
	
	this.getId = function () {return this.id;}
	this.getName = function () {return this.name;}
	this.getDescription = function () {return this.description;}
	this.getAccessionNumber = function () {return this.accessionNumber;}
	this.getGroups = function () {return this.groups;}
	this.getChemblId = function () {return this.chembl_id;}
	this.getIndication = function () {return this.indication;}
	this.getMechanismOfAction = function () {return this.mechanismOfAction;}
	this.getMetabolism = function () {return this.metabolism;}
	this.getProteinBinding = function () {return this.proteinBinding;}
	this.getRouteOfElimination = function () {return this.routeOfElimination;}
	this.getRoutes = function () {return this.routes;}
	this.getSmile = function () {return this.smile;}
	this.getSynonyms = function () {return this.synonyms;}
	this.getToxicity = function () {return this.toxicity;}
	this.getType = function () {return this.type;}
	

	this.toString = function () {
		var drugString ="id="+this.getId()+" name="+this.getName()+" description="+this.getDescription()+" accessionNumber="+this.getAccessionNumber()+" groups="+this.getGroups()+" chembl_id="+this.getChemblId()+" indication="+this.getIndication()+" mechanismOfAction="+this.getMechanismOfAction()+" metabolism="+this.getMetabolism()+" proteinBinding="+this.getProteinBinding()+" routeOfElimination="+this.getRouteOfElimination()+" routes="+this.getRoutes()+" smile="+this.getSmile()+" synonyms="+this.getSynonyms()+" toxicity="+this.getToxicity()+" type="+this.getType();
		return drugString;
	}
}
