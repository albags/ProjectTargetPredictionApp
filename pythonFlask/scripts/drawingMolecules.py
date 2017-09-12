#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
/* @DrawingMolecules()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Draw 2D molecule object
* @Attributes:
* 		mol;
* @methods:
* 		__init__ (construct): prepares the molecule for moments calculs
* 		drawMoleculeQuery
* 		drawMoleculeSimilar
*/
"""

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import os
import shutil

class DrawingMolecules(object):
	def __init__(self, smile):
		self.mol = Chem.MolFromSmiles(smile)
		return

	"""
	Creates the molecule 2D image and save it
	"""
	def drawMoleculeQuery(self):
		size = (400, 400)
		# fig = Draw.MolToMPL(self.mol, size=size)
		img = Draw.MolToImage(self.mol, size=size)
		img.save('static/images/queryMolecule/queryMolecule.png')
		return

	"""
	Creates them molecule 2D image for similar molecule and save it
	"""
	def drawMoleculeSimilar(self, moleculeName):
		# empty folder
		directory = 'static/images/similarityResultsImgs/'
		size = (400, 400)
		img = Draw.MolToImage(self.mol, size=size)
		img.save(directory+moleculeName+'.png')
		return


	

# O=C(Oc1ccccc1C(=O)O)C
# C[C@H](O)[C@H](C)[C@@H]1O[C@H]1C[C@H]2CO[C@@H](C\\C(=C\\C(=O)OCCCCCCCCC(=O)O)\\C)[C@H](O)[C@@H]2O