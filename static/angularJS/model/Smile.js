/* @Smile()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Object review
* @Attributes:
* 		id: id number;
		name;
		smile;
* @methods:
* 		construct
* 		set's and get's foor each attribute
*		toString: return a string with all object's information
*/

function Smile () {
	//Attributes declaration
	this.id;
	this.name;
	this.smile;

	//Methods declaration
	this.construct = function (id,name,smile) {
		this.setId(id);
		this.setName(name);
		this.setSmile(smile);
	}

	this.setId = function (id){this.id=id;}
	this.setName = function (name){this.name=name;}
	this.setSmile = function (smile){this.smile=smile;}

	this.getId = function () {return this.id;}
	this.getName = function () {return this.name;}
	this.getSmile = function () {return this.smile;}

	this.toString = function () {
		var smileString = "id="+this.getId()+" name="+this.getName()+" surname="+this.getSmile();

		return smileString;
	}

}
