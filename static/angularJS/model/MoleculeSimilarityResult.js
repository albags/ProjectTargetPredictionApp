/* @MoleculeSimilarityResult()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Object molecule similarity results
* @Attributes:
* 		id: id number;
*		smile;
* 		chembl_id;
* 		similarity;
* @methods:
* 		construct
* 		set's and get's for each attribute
*		toString: return a string with all object's information
*/

function MoleculeSimilarityResult () {
	//Attributes declaration
	this.id;
	this.smile;
	this.chembl_id;
	this.similarity;

	//Methods declaration
	this.construct = function (id, smile, chembl_id, similarity) {
		this.setId(id);
		this.setSmile(smile);
		this.setChemblId(chembl_id);
		this.setSimilarity(similarity);
	}

	this.setId = function (id){this.id=id;}
	this.setSimilarity = function (similarity){this.similarity=similarity;}
	this.setSmile = function (smile){this.smile=smile;}
	this.setChemblId = function (chembl_id){this.chembl_id=chembl_id;}

	this.getId = function () {return this.id;}
	this.getSimilarity = function () {return this.similarity;}
	this.getSmile = function () {return this.smile;}
	this.getChemblId = function () {return this.chembl_id;}

	this.toString = function () {
		var similarityString ="id="+this.getId()+" smile="+this.getSmile()+" chembl_id="+this.getChemblId()+" similarity="+this.getSimilarity();

		return similarityString;
	}
}
