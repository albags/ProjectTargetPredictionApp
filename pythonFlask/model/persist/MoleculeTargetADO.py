#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
/* @TargetADO()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: access data object for targets management
* @Attributes:
* 		organism;
* 		smile;
* 		query;
* @methods:
* 		__init__ (construct)
* 		findByQuery
* 		findTargets
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
from DBConnect import DBConnect
from MoleculeTarget import MoleculeTarget


class TargetADO(object):
	# Constructor
	def __init__(self, organism, smile):
		self.organism = organism
		self.smile = smile
		self.query = "SELECT GROUP_CONCAT(DISTINCT td.pref_name SEPARATOR ', '), GROUP_CONCAT(DISTINCT syn.component_synonym SEPARATOR ', '), GROUP_CONCAT(DISTINCT cs.accession SEPARATOR ', '), td.chembl_id, GROUP_CONCAT(DISTINCT pcg.target_classification SEPARATOR ', ') FROM protein_classification_groups pcg, target_dictionary td, target_components tc, component_sequences cs, component_synonyms syn, component_class cc, protein_classification pc, assays a, activities act, molecule_dictionary md, compound_structures cos WHERE pcg.id=pc.target_class_id AND td.tid = tc.tid AND tc.component_id = cs.component_id AND cs.component_id = syn.component_id AND cs.component_id = cc.component_id AND cc.protein_class_id = pc.protein_class_id AND td.organism = '%s' AND td.tid = a.tid AND a.assay_id = act.assay_id AND act.molregno = md.molregno AND md.molregno = cos.molregno AND cos.canonical_smiles = '%s' GROUP BY td.chembl_id" 
		return

	"""
	Connects to the database and execute the query to find all targets for the molecule query in the organism given
	Returns a list with all the molecules with targets
	"""
	def findByQuery (self, query):
		conn = DBConnect()
		data = conn.executionQueryTargets(query, self.organism, self.smile)
		return data

	"""
	Calls the method that executes the query for finding the targets
	Return data found
	"""
	def findTargets (self):
		return self.findByQuery(self.query)

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
			d['target'] = row[0]
			d['gene_name'] = row[1]
			d['uniprot_id'] = row[2]
			d['chembl_id'] = row[3]
			d['target_class'] = row[4]
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

	
