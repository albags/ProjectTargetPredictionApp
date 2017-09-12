/* @MoleculeSimilarityForm()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Object molecule query for similarities calculs
* @Attributes:
* 		id: id number;
*		smile;
* 		typeSimilarity;
* @methods:
* 		construct
* 		set's and get's for each attribute
*		toString: return a string with all object's information
*/

function MoleculeSimilarityForm () {
	//Attributes declaration
	this.id;
	this.smile;
	this.typeSimilarity;

	//Methods declaration
	this.construct = function (id,smile,typeSimilarity) {
		this.setId(id);
		this.setSmile(smile);
		this.setTypeSimilarity(typeSimilarity);
	}

	this.setId = function (id){this.id=id;}
	this.setTypeSimilarity = function (typeSimilarity){this.typeSimilarity=typeSimilarity;}
	this.setSmile = function (smile){this.smile=smile;}

	this.getId = function () {return this.id;}
	this.getTypeSimilarity = function () {return this.typeSimilarity;}
	this.getSmile = function () {return this.smile;}

	this.toString = function () {
		var similarityString ="id="+this.getId()+" smile="+this.getSmile()+" typeSimilarity="+this.getTypeSimilarity();

		return similarityString;
	}
}
