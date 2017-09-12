#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
/* @MoleculeDrug()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Object molecule query for drug information
* @Attributes:
* 		id: id number;
*		moleculeId: drugbank id or accession number;
* @methods:
* 		__init__ (construct)
* 		set's and get's for each attribute
* 		toJSON: transform the object to json format 
* 		toObj: put the objects in a list to jsonify them 
*/
"""

import warnings
from switch import Switch
import json
import time
import datetime
import collections


class MoleculeDrug(object):
	def __init__(self, id, moleculeId):
		self.id = id
		self.moleculeId = moleculeId

	def toJSON(self, obj):
		obj1 = json.dumps(obj)
		obj1 = json.loads(obj1)
		return obj1

	def toObj(self, rows):
		objects_list = []
		for row in rows:
			d = collections.OrderedDict()
			d['id'] = row[0]
			d['moleculeId'] = row[1]
			objects_list.append(d)
		j = self.toJSON(objects_list)
		return j

	def getId(self):
		return self.id

	def getMoleculeId(self):
		return self.moleculeId

	def setId(self, id):
		self.id = id

	def setMoleculeId(self, moleculeId):
		self.moleculeId = moleculeId