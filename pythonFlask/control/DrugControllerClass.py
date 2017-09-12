#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
/* @DrugController()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Drug information controller
* @Attributes:
* 		action: action number;
*		jsonData: molecule query;
* @methods:
* 		__init__ (construct)
* 		doAction
*		drugConnection
*		drawMol
*/
"""

from switch import Switch
import sys
import os
import shutil

sys.path.append('./pythonFlask/model')
sys.path.append('./pythonFlask/model/persist')
sys.path.append('./pythonFlask/scripts')
from MoleculeDrugADO import DrugADO
from drawingMolecules import DrawingMolecules


class DrugController (object):
	def __init__(self, action, jsonData):
		self.action = action
		self.jsonData = jsonData
	
	"""
	Switch for all the action's possibilities/cases
	Returns the drug Object to the main controller
	"""
	def doAction(self):
		drugConnection = []

		with Switch(self.action) as case:
			if case(10000):
				drugInfo = self.drugConnection()
				if (drugInfo != {}):
					print drugInfo['smile']
					self.drawMol(drugInfo)
				# break
			
			if case.default:
				print "\nOption not correct in DrugControllerClass.py\n"

		return drugInfo

	"""
	Connects to the access data object to find the drug information 
	Returns a drug Object
	"""
	def drugConnection(self): 
		drugADO = DrugADO(self.jsonData['moleculeId'])
		data = drugADO.findDrug()
		drugInfo = drugADO.dataToObj(data)
		return drugInfo

	"""
	Sends the smile molecule to Draw object to save the image
	"""
	def drawMol(self, drugInfo):
		drawMolecule = DrawingMolecules(drugInfo['smile'])
		drawMolecule.drawMoleculeQuery()
		return