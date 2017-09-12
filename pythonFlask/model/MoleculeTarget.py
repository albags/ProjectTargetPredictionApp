#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
/* @MoleculeTarget()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Object molecule query for target information
* @Attributes:
* 		id: id number;
*		organism;
*		smile;
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


class MoleculeTarget(object):
	def __init__(id, organism, smile):
		self.id = id
		self.organism = organism
		self.smile = smile

	def toJSON(self, obj):
		obj1 = json.dumps(obj)
		obj1 = json.loads(obj1)
		return obj1

	def toObj(self, rows):
		objects_list = []
		for row in rows:
			d = collections.OrderedDict()
			d['id'] = row[0]
			d['organism'] = row[1]
			d['smile'] = row[2]
			objects_list.append(d)
		j = self.toJSON(objects_list)
		return j

	def getId(self):
		return self.id

	def getOrganim(self):
		return self.organism

	def getSmile(self):
		return self.smile

	def setId(self,id):
		self.id = id

	def setOrganim(self,organism):
		self.organism = organism

	def setSmile(self,smile):
		self.smile = smile