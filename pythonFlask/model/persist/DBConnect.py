#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
/* @DBConnect()
* @author: Alba Gómez Segura 
* @date: 01/02/2017
* @description: Connection to the database source
* @Attributes:
* 		server;
*		user;
*		password;
*		dataBase;
* @methods:
* 		__init__ (construct)
* 		connect
* 		close
* 		executionQueryTargets
* 		executionQuerySimilarity
*/
"""

import warnings
import os
from switch import Switch
import json
import _mysql
import sys
import MySQLdb

class DBConnect(object):
	def __init__(self):       
		self.server = "database"
		self.user  = "alba"
		self.password  = "bobYpal2"
		self.dataBase  = "project_fda"
		# self.dataBase  = "chembl22_1"
		return

	"""
	Mysql connection to the database
	"""
	def connect(self):
		try:
			self.db = MySQLdb.connect(self.server, self.user, self.password, self.dataBase)
			# print "Connected successfully Project!!!\n"
		except:
			print("Database does not exist")
		return

	"""
	Close mysql connection 
	"""
	def close(self):
		if (self.db):
			self.cursor.close()
			del self.cursor
			self.db.close()
		return

	"""
	Executes the targets query
	Returns data which is a list with targets found if there are any
	"""
	def executionQueryTargets(self, query, organism, smile): 
		data = []
		self.connect()
		self.cursor = self.db.cursor()
		try:
			self.cursor.execute(query % (organism, smile))
			data = self.cursor.fetchall()
		except Exception as e:
			print "Error: ", e
			print "Query: ", query
		finally:
			self.close()
		return data

	"""
	Executes the similarity query
	Returns cleanData which is a list with similar molecules if there are any
	"""
	def executionQuerySimilarity(self, query): 
		data = []
		cleanData = []
		self.connect()
		self.cursor = self.db.cursor()
		try:
			self.cursor.execute(query)
			data = self.cursor.fetchall()
			for info in data:
				cleanData.append(info)
		except Exception as e:
			print "Error: ", e
			print "Query: ", query
		finally:
			self.close()
		return cleanData
	