#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
/* @DrugADO()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: access data object for drug management
* @Attributes:
* 		moleculeId: drugbank id or accession number;
* @methods:
* 		__init__ (construct)
* 		findDrug
* 		dataToObj
* 		toJSON
*/
"""

import warnings
import os
from switch import Switch
import json
import collections
import json
from rdkit.Chem import Draw

import sys
sys.path.append('./pythonFlask/model')
sys.path.append('./pythonFlask/model/persist')
from DBConnect import DBConnect
from DBConnectDrugBank import DBConnectDrugBank
from MoleculeDrug import MoleculeDrug


class DrugADO(object):
	# Constructor
	def __init__(self, moleculeId):
		self.moleculeId = moleculeId
		return

	"""
	Connects to the database
	Returns the molecule query found
	"""
	def findDrug (self):
		conn = DBConnectDrugBank()
		data = conn.findInfoDrug(self.moleculeId)
		return data

	"""
	Calls the json method
	Return object in json format
	"""
	def dataToObj (self, data):
		drugInfo = self.toJSON(data)
		return drugInfo

	"""
	Transform object to json format
	Return object in json format
	"""
	def toJSON(self, obj):
		obj1 = json.dumps(obj)
		obj1 = json.loads(obj1)
		return obj1

	
