#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
/* @SimilarityADO()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: access data object for similarity management
* @Attributes:
* 		smile;
* 		typeSimilarity;
* 		listAllSmiles: list with all the smiles in chembl database;
* 		query;
* @methods:
* 		__init__ (construct)
* 		findByQuery
* 		find_simils
* 		findFingerprints
* 		findFingerprintsSimilarity
* 		findUsrcatSimilarity
* 		findElectroshapeSimilarity
* 		dataToObj
* 		toJSON
* 		toObj
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
sys.path.append('./pythonFlask/scripts')
from DBConnect import DBConnect
from MoleculeSimilarity import MoleculeSimilarity
from FingerprintsClass import FingerprintsClass
from UsrcatClass import UsrcatClass
from ElectroshapeClass import ElectroshapeClass


class SimilarityADO(object):
	# Constructor
	def __init__(self, smile, typeSimilarity):
		self.smile = smile
		self.typeSimilarity = typeSimilarity
		self.listAllSmiles = []
		self.query = "SELECT cd.chembl_id, cs.canonical_smiles FROM molecule_dictionary cd, compound_structures cs WHERE cd.molregno = cs.molregno AND cs.canonical_smiles IS NOT NULL"
		return

	"""
	Connects to the database and execute the query to find all the smiles in the database
	Returns a list with all the molecules with smiles in the database
	"""
	def findByQuery (self):
		conn = DBConnect()
		self.listAllSmiles = conn.executionQuerySimilarity(self.query)
		return self.listAllSmiles

	"""
	Executes FingerprintsClass similarity function with reference molecule and comparation molecule
	Returns percentatge of similarity
	"""
	def find_simils(self, refSmile, smile):
		simil = False
		try: 
			m = FingerprintsClass(smile, input_type="smile")
			simil = refSmile.is_similar(m) 
		except Exception as e:
			print "Error: ", e
		return simil

	"""
	Executes FingerprintsClass to find similarities between molecules
	Return list with reference molecule, comparation molecule and percentatge of similarity
	"""
	def findFingerprints(self):
		listFp = []
		refSmile = FingerprintsClass(self.smile)
		for smi in self.listAllSmiles:
			similarity = self.find_simils(refSmile, smi[1]) # listAllSmiles és una llista de llistes
			if similarity != False:
				listFp.append([smi[0], smi[1], round(similarity, 4)])
		return listFp;

	"""
	Calls the fingerprint method
	Returns a list with all the similar molecules calculate with fingerprint method
	"""
	def findFingerprintsSimilarity (self):
		listFp = []
		listFp = self.findFingerprints()
		return listFp

	"""
	Executes UsrcatClass to calculs moments of ligand and conformers to find the similarity between them
	Returns a list with all the similar molecules calculate with usrcat method where the percentatge of similarity is upper than the 0.5
	"""
	def findUsrcatSimilarity (self):
		ligand = UsrcatClass(self.smile);
		ligand.calc_moments()

		similarities = []
		i = 0
		for smi in self.listAllSmiles:
			try:
				conformer = UsrcatClass(smi[1])
				conformer.calc_moments()
				similarity = ligand.find_similarity(conformer)
				if (similarity > 0.5):
					similarities.append([smi[0], smi[1], round(similarity, 4)])
				i += 1
				if (i > 10):
					break
			except AttributeError as e:
				print "\nAttributeError: %s" % e
			except ValueError as e:
				print "\nValueError: %s" % e
			except Exception as e:
				print "General error: %s" % e
		return similarities

	"""
	Executes ElectroshapeClass to calculs moments of ligand and conformers to find the similarity between them
	Returns a list with all the similar molecules calculate with electroshape method where the percentatge of similarity is upper than the 0.5
	"""
	def findElectroshapeSimilarity (self):
		ligand = ElectroshapeClass(self.smile);
		ligand.calc_moments()

		similarities = []
		i = 0
		for smi in self.listAllSmiles:
			try:
				conformer = ElectroshapeClass(smi[1])
				conformer.calc_moments()
				similarity = ligand.find_similarity(conformer)
				if (similarity > 0.5):
					similarities.append([smi[0], smi[1], round(similarity, 4)])
				i += 1
				if (i > 10):
					break
			except AttributeError as e:
				print "\nAttributeError: %s" % e
			except ValueError as e:
				print "\nValueError: %s" % e
			except Exception as e:
				print "\nGeneral error: %s" % e
		return similarities

	"""
	Calls the json method
	Return object in json format
	"""
	def dataToObj (self, data):
		targets = self.toObj(data)
		return targets

	"""
	Converts list to json format
	Return object in json format
	"""
	def toObj(self, rows):
		objects_list = []
		for row in rows:
			d = collections.OrderedDict()
			d['chembl_id'] = row[0]
			d['smile'] = row[1]
			d['similarity'] = row[2]
			objects_list.append(d)
		j = self.toJSON(objects_list)
		return j

	"""
	Transform object to json format
	Return object in json format
	"""
	def toJSON(self, obj):
		obj1 = json.dumps(obj)
		obj1 = json.loads(obj1)
		return obj1

	
