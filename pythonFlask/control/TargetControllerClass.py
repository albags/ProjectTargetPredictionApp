#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
/* @TargetController()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Molecule targets prediction controller
* @Attributes:
* 		action: action number;
*		jsonData: molecule query;
* @methods:
* 		__init__ (construct)
* 		doAction
*		targetConnection
*		drawMol
*/
"""

from switch import Switch
import sys
import os
import shutil
import plotly.plotly as py
import plotly.graph_objs as go

sys.path.append('./pythonFlask/model')
sys.path.append('./pythonFlask/model/persist')
sys.path.append('./pythonFlask/scripts')
from MoleculeTargetADO import TargetADO
from drawingMolecules import DrawingMolecules


class TargetController (object):
	def __init__(self, action, jsonData):
		self.action = action
		self.jsonData = jsonData
	
	"""
	Switch for all the action's possibilities/cases
	Returns the similar molecules Objects to the main controller
	"""
	def doAction(self):
		targetConnection = []

		with Switch(self.action) as case:
			if case(10000):
				targets = self.targetConnection()
				self.drawMol()
				# break
			
			if case.default:
				print "\nOption not correct in TargetControllerClass.py\n"

		return targets

	"""
	Connects to access data object
	Returns a list with target Objects
	"""
	def targetConnection(self): 
		targetADO = TargetADO(self.jsonData['organism'], self.jsonData['smile'])
		data = targetADO.findTargets()
		targetsInfo = targetADO.dataToObj(data)
		return targetsInfo

	"""
	Sends the smile molecule to Draw object to save the image
	"""
	def drawMol(self):
		drawMolecule = DrawingMolecules(self.jsonData['smile'])
		drawMolecule.drawMoleculeQuery()
		return