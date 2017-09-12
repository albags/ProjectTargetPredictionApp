/* @MoleculeTargetResult()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Object molecule target results
* @Attributes:
* 		id: id number;
*		target;
* 		gene_name;
* 		uniprot_id;
*		chembl_id;
* 		target_class;
* @methods:
* 		construct
* 		set's and get's for each attribute
*		toString: return a string with all object's information
*/

function MoleculeTargetResult () {
	//Attributes declaration
	this.id;
	this.target;
	this.gene_name;
	this.uniprot_id;
	this.chembl_id;
	this.target_class;

	//Methods declaration
	this.construct = function (id, target, gene_name, uniprot_id, chembl_id, target_class) {
		this.setId(id);
		this.setTarget(target);
		this.setGeneName(gene_name);
		this.setUniprotId(uniprot_id);
		this.setChemblId(chembl_id);
		this.setTargetClass(target_class);
	}

	this.setId = function (id){this.id=id;}
	this.setTarget = function (target){this.target=target;}
	this.setGeneName = function (gene_name){this.gene_name=gene_name;}
	this.setUniprotId = function (uniprot_id){this.uniprot_id=uniprot_id;}
	this.setChemblId = function (chembl_id){this.chembl_id=chembl_id;}
	this.setTargetClass = function (target_class){this.target_class=target_class;}

	this.getId = function () {return this.id;}
	this.getTarget = function () {return this.target;}
	this.getGeneName = function () {return this.gene_name;}
	this.getUniprotId = function () {return this.uniprot_id;}
	this.getChemblId = function () {return this.chembl_id;}
	this.getTargetClass = function () {return this.target_class;}

	this.toString = function () {
		var targetString ="id="+this.getId()+" target_name="+this.getTarget()+" gene_name="+this.getGeneName()+" uniprot_id="+this.getUniprotId()+" chembl_id="+this.getChemblId()+" target_class="+this.getTargetClass();

		return targetString;
	}
}
