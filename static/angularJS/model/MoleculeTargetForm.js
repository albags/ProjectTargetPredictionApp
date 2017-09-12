/* @MoleculeTargetForm()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Object molecule query for targets
* @Attributes:
* 		id: id number;
*		organism;
* 		smile;
* @methods:
* 		construct
* 		set's and get's for each attribute
*		toString: return a string with all object's information
*/

function MoleculeTargetForm () {
	//Attributes declaration
	this.id;
	this.organism;
	this.smile;

	//Methods declaration
	this.construct = function (id, organism, smile) {
		this.setId(id);
		this.setOrganism(organism);
		this.setSmile(smile);
	}

	this.setId = function (id){this.id=id;}
	this.setOrganism = function (organism){this.organism=organism;}
	this.setSmile = function (smile){this.smile=smile;}

	this.getId = function () {return this.id;}
	this.getOrganism = function () {return this.organism;}
	this.getSmile = function () {return this.smile;}

	this.toString = function () {
		var targetString ="id="+this.getId()+" name="+this.getOrganism()+" surname="+this.getSmile();

		return targetString;
	}
}
