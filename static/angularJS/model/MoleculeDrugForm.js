/* @MoleculeDrugForm()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Object molecule query for drug information
* @Attributes:
* 		id: id number;
*		name;
* @methods:
* 		construct
* 		set's and get's for each attribute
*		toString: return a string with all object's information
*/

function MoleculeDrugForm () {
	//Attributes declaration
	this.id;
	this.moleculeId;

	//Methods declaration
	this.construct = function (id, moleculeId) {
		this.setId(id);
		this.setMoleculeId(moleculeId);
	}

	this.setId = function (id){this.id=id;}
	this.setMoleculeId = function (moleculeId){this.moleculeId=moleculeId;}

	this.getId = function () {return this.id;}
	this.getMoleculeId = function () {return this.moleculeId;}

	this.toString = function () {
		var drugString ="id="+this.getId()+" moleculeId="+this.getMoleculeId();
		return drugString;
	}
}
