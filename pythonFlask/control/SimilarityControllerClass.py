#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
/* @SimilarityController()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Similarity Object controller
* @Attributes:
* 		action: action number;
*		jsonData: molecule query;
* @methods:
* 		__init__ (construct)
* 		doAction
*		similarityConnection
*		drawMol
*		drawMolSim
*/
"""

from switch import Switch
import sys
import os
import shutil

sys.path.append('./pythonFlask/model')
sys.path.append('./pythonFlask/model/persist')
sys.path.append('./pythonFlask/scripts')
from MoleculeSimilarityADO import SimilarityADO
from drawingMolecules import DrawingMolecules

class SimilarityController (object):
	def __init__(self, action, jsonData):
		self.action = action
		self.jsonData = jsonData
	
	"""
	Switch for all the action's possibilities/cases
	Returns the similar molecules Objects to the main controller
	"""
	def doAction(self):
		similarMols = []

		with Switch(self.action) as case:
			if case(10000):
				similarMols = self.similarityConnection()
				# Clean directory for similar molecules
				directorySim = 'static/images/similarityResultsImgs/'
				shutil.rmtree(directorySim)
				os.makedirs(directorySim)
				self.drawMol()
				for mol in similarMols:
					self.drawMolSim(mol)
				# break
			
			if case.default:
				print "\nOption not correct in TargetControllerClass.py\n"

		return similarMols

	"""
	Checks which type of similarity the user wants to calculate and connects to access data object
	Returns a list with similar molecules Objects
	"""
	def similarityConnection(self): 
		similarityADO = SimilarityADO(self.jsonData['smile'], self.jsonData['typeSimilarity'])
		similarityADO.findByQuery()
		
		if (self.jsonData['typeSimilarity'] == "fingerprint"):
			data = similarityADO.findFingerprintsSimilarity()
		elif (self.jsonData['typeSimilarity'] == "electroshape"):
			data = similarityADO.findElectroshapeSimilarity()
		elif (self.jsonData['typeSimilarity'] == "usrcat"):
			data = similarityADO.findUsrcatSimilarity()
		else:
			return "Error similarity method"

		similarMolsInfo = similarityADO.dataToObj(data)
		return similarMolsInfo

	"""
	Sends the smile molecule to Draw object to save the image
	"""
	def drawMol(self):
		drawMolecule = DrawingMolecules(self.jsonData['smile'])
		drawMolecule.drawMoleculeQuery()
		return

	"""
	Sends the smile of the similar molecules to Draw objects and save the images
	"""
	def drawMolSim(self, mol):
		drawMolecule = DrawingMolecules(mol['smile'])
		drawMolecule.drawMoleculeSimilar(mol['chembl_id'])
		return