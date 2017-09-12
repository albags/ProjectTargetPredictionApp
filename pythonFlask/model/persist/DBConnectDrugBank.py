#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
/* @DBConnectDrugBank()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Connection to the drugbank xml database
* @Attributes:
* 		server;
*		user;
*		password;
*		dataBase;
* @methods:
* 		__init__ (construct)
* 		unique_list
* 		findInfoDrug
*/
"""

import warnings
import json
import collections
from lxml import etree
import csv
import sys
import re
import io

reload(sys)
sys.setdefaultencoding('utf8')

class DBConnectDrugBank(object):
	def __init__(self):
		self.tree = etree.parse('./databases/resum_database.xml')
		self.root = self.tree.getroot()
		return

	"""
	Erases duplicates in a list
	Return list without duplicate registers
	"""
	def unique_list(self, l):
		ulist = []
		[ulist.append(x) for x in l if x not in ulist]
		return ulist

	"""
	Parses the xml to find the query molecule
	Returns drugInfo which is a dict with drug information if molecule exists
	"""
	def findInfoDrug(self, identifier):
		drugInfo = {}
		for d in self.root.findall("drug"):
			drugbank_id = ""
			name = ""
			type = ""
			description = ""
			group = ""
			synonym = ""
			route = ""
			smile = ""
			indication = ""
			protein_binding = ""
			route_of_elimination = ""
			metabolism = ""
			mechanism_of_action = ""
			toxicity = ""
			external_identifier = ""

			if (d.find('drugbank-id').text == identifier):
				drugbank_id = d.find('drugbank-id').text
				if drugbank_id is not None:
					drugbank_id = re.sub('\s+',' ',drugbank_id)
				else:
					drugbank_id = " "
				drugInfo["drugbank-id"] = drugbank_id

				name = d.find('name').text
				if name is not None:
					name = re.sub('\s+',' ',name)
				else:
					name = " "
				drugInfo["name"] = name

				type = d.find('type').text
				if type is not None:
					type = re.sub('\s+',' ',type)
				else:
					type = " "
				drugInfo["type"] = type

				description = d.find('description').text
				if description is not None:
					description = re.sub('\s+',' ',description)
				else:
					description = " "
				drugInfo["description"] = description

				for g in d.findall("groups/group"):
					group += g.text + "; "
				if group is not None:
					group = "; ".join(self.unique_list(group.split("; ")))
					group = re.sub('\s+',' ',group)
				else:
					group = " "
				drugInfo["groups"] = group

				for s in d.findall('synonyms/synonym'):
					synonym += s.text + "; "
				if synonym is not None:
					synonym = "; ".join(self.unique_list(synonym.split("; ")))
					synonym = re.sub('\s+',' ',synonym)
				else:
					synonym = " "
				drugInfo["synonyms"] = synonym

				for r in d.findall('products/product/route'):
					if r.text is not None:
						route += r.text + "; "
				if route is not None:
					route = "; ".join(self.unique_list(route.split("; ")))
					route = re.sub('\s+',' ',route)
				else:
					route = " "
				drugInfo["routes"] = route

				# smile = d.find('calculated-properties/property[kind="SMILES"]/value').txt
				smile = d.find('calculated-properties/property/value').text
				if smile is not None:
					smile = re.sub('\s+',' ',smile)
				else:
					smile = " "
				drugInfo["smile"] = smile

				indication = d.find('indication').text
				if indication is not None:
					indication = re.sub('\s+',' ',indication)
					indication = indication.replace("<i>", "")
					indication = indication.replace("</i>", "")
				else:
					indication = " "
				drugInfo["indication"] = indication

				protein_binding = d.find('protein-binding').text
				if protein_binding is not None:
					protein_binding = re.sub('\s+',' ',protein_binding)
				else:
					protein_binding = " "
				drugInfo["protein-binding"] = protein_binding

				route_of_elimination = d.find('route-of-elimination').text
				if route_of_elimination is not None:
					route_of_elimination = re.sub('\s+',' ',route_of_elimination)
				else:
					route_of_elimination = " "
				drugInfo["route-of-elimination"] = route_of_elimination

				metabolism = d.find('metabolism').text
				if metabolism is not None:
					metabolism = re.sub('\s+',' ',metabolism)
				else:
					metabolism = " "
				drugInfo["metabolism"] = metabolism

				mechanism_of_action = d.find('mechanism-of-action').text
				if mechanism_of_action is not None:
					mechanism_of_action = re.sub('\s+',' ',mechanism_of_action)
				else:
					mechanism_of_action = " "
				drugInfo["mechanism-of-action"] = mechanism_of_action

				toxicity = d.find('toxicity').text
				if toxicity is not None:
					toxicity = re.sub('\s+',' ',toxicity)
				else:
					toxicity = " "
				drugInfo["toxicity"] = toxicity

				external_identifier = d.find('external-identifiers/identifier').text
				if external_identifier is not None:
					external_identifier = re.sub('\s+',' ',external_identifier)
				else:
					external_identifier = " "
				drugInfo["identifier"] = external_identifier

		return drugInfo

