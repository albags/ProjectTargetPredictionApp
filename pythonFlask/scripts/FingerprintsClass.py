#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
/* @FingerprintsClass()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: fingerprints molecule object
* @Attributes:
*		mol: construct a molecule from a SMILES string;
* 		HBD: the number of H-bond donors for a molecule;
* 		Wt: molecule's exact molecular weight;
*		NumRotatableBonds: number of rotatable bonds for a molecule;
* 		HBA: number of H-bond acceptors for a molecule;
* 		logP: 2-tuple with the Wildman-Crippen logp,mr values;
* 		FingerPrint: topological fingerprint for a molecule;
* @methods:
* 		__init__ (construct): prepares the molecule for moments calculs
* 		compute_HBD
* 		compute_Wt
* 		compute_NumRotatableBonds
* 		compute_HBA
* 		compute_logP
* 		compute_fingerprin
* 		compute_similarity
* 		is_similar
*/
"""

import sys
from rdkit import Chem
from decimal import Decimal
from rdkit.Chem import rdMolDescriptors
from rdkit import DataStructs
from rdkit.Chem.Fingerprints import FingerprintMols
import os


# Default values:
HBD_t = 1
MW_t = 25
RB_t = 1
HBA_t = 2
ClogP_t = float(Decimal(1))#1.5
tanimoto_t_min = Decimal('0.70')
tanimoto_t_max = Decimal('1')

class FingerprintsClass(object):
	def __init__(self, mol_input, input_type = "smile"):
		self.mol = Chem.MolFromSmiles(mol_input)
		self.HBD = self.compute_HBD(self.mol)
		self.Wt = self.compute_Wt(self.mol)
		self.NumRotatableBonds = self.compute_NumRotatableBonds(self.mol)
		self.HBA = self.compute_HBA(self.mol)
		self.logP = self.compute_logP(self.mol)
		self.FingerPrint = self.compute_fingerprint(self.mol)
	"""
	Returns the number of H-bond donors for a molecule
	"""
	def compute_HBD(self, mol_input):
		return rdMolDescriptors.CalcNumHBD(mol_input)
	
	"""
	Returns the molecule's exact molecular weight
	"""
	def compute_Wt(self, mol_input):
		return rdMolDescriptors.CalcExactMolWt(mol_input)

	"""
	Returns the number of rotatable bonds for a molecule
	"""
	def compute_NumRotatableBonds(self, mol_input):
		return rdMolDescriptors.CalcNumRotatableBonds(mol_input)

	"""
	Returns the number of H-bond acceptors for a molecule
	"""
	def compute_HBA(self, mol_input):
		return rdMolDescriptors.CalcNumHBA(mol_input)

	"""
	Returns a 2-tuple with the Wildman-Crippen logp,mr values
	"""
	def compute_logP(self, mol_input):
		logP, mr = rdMolDescriptors.CalcCrippenDescriptors(mol_input)
		return logP

	"""
	Returns a topological fingerprint for a molecule
	"""
	def compute_fingerprint(self, mol_input):
		return FingerprintMols.FingerprintMol(mol_input)
	
	"""
	Returns the calculated similarity between two fingerprints
	"""
	def compute_similarity(self, mol_input):
		return DataStructs.FingerprintSimilarity(self.FingerPrint, mol_input.FingerPrint, metric=DataStructs.TanimotoSimilarity)
	
	"""
	Returns a boolean rather if two molecules are enough similar
	"""
	def is_similar(self, mol_input):
		if self.HBD - HBD_t <= mol_input.HBD <= self.HBD + HBD_t:
			if self.Wt - MW_t <= mol_input.Wt <= self.Wt + MW_t:
				if self.NumRotatableBonds - RB_t <= mol_input.NumRotatableBonds <= self.NumRotatableBonds + RB_t:
					if self.HBA - HBA_t <= mol_input.HBA <= self.HBA + HBA_t :
						if self.logP - ClogP_t <= mol_input.logP <= self.logP + ClogP_t:
							if tanimoto_t_min <= self.compute_similarity(mol_input) <= tanimoto_t_max:
								return self.compute_similarity(mol_input)
		return False

	
	
	


	
