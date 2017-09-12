#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
/* @ElectroshapeClass()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: electroshape molecule object
* @Attributes:
* 		smile;
* 		input_type;
* @methods:
* 		__init__ (construct): prepares the molecule for moments calculs
* 		calc_moments
* 		find_similarity
*/
"""

from electroshape.toolkits.rd import generate_moments
from electroshape import similarity
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

class ElectroshapeClass(object):
	def __init__(self, smile, input_type = "smile"):
		self.molObj = Chem.MolFromSmiles(smile)
		# AllChem.EmbedMolecule(self.molObj, useExpTorsionAnglePrefs=True, useBasicKnowledge=True, randomSeed=1, useRandomCoords=False, maxAttempts=5, randNegEig=1, enforceChirality=True)
		AllChem.EmbedMultipleConfs(self.molObj, useExpTorsionAnglePrefs=True, useBasicKnowledge=True, randomSeed=1, useRandomCoords=False, maxAttempts=5, randNegEig=1, enforceChirality=True)
		self.moments = []
		return

	"""
	Calculates the moments for a molecule
	"""
	def calc_moments(self):
		#Generate moments for the content of each file
		self.moments = np.array(generate_moments(self.molObj))
		return

	"""
	Finds the similarity for betwwen the difference conformers
	Retuns the maximum similarity found
	"""
	def find_similarity(self, conformer):
		# Calcule similarities for each crystal ligand with all his conformers (actives and decoys)
		simil = 0
		similar = []
		max_sim = 0
		try:
			for i in range(len(self.moments)):
				for j in range(len(conformer.moments)):
					simil = similarity.es_sim_score(self.moments[i], conformer.moments[j])
					similar.append(simil)
			max_sim = max(similar)
		except ValueError as e:
			print "\nValueError find_similarity: %s" % e
		except Exception as e:
			print "\nGeneral error calculating similarity: %s" % e

		return max_sim


# O=C(Oc1ccccc1C(=O)O)C
# C[C@H](O)[C@H](C)[C@@H]1O[C@H]1C[C@H]2CO[C@@H](C\\C(=C\\C(=O)OCCCCCCCCC(=O)O)\\C)[C@H](O)[C@@H]2O