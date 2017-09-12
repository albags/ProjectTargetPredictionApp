#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from flask import Flask, render_template, jsonify, json, request, session, flash, redirect

import os
import sys
import time
import numpy as np
import json

sys.path.append('pythonFlask/control')
from TargetControllerClass import TargetController
from SimilarityControllerClass import SimilarityController
from DrugControllerClass import DrugController

app = Flask(__name__) # , template_folder='view'
app.secret_key = 'any random string'

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/targetsForm')
def targetsForm():
	iframe = "/static/angularJS/iframe/demo.html"
	return render_template("compound-target-form.html", iframe = iframe)

@app.route('/similarityForm')
def similarityForm():
	hora = time.time()
	iframe = "/static/angularJS/iframe/demo.html"
	return render_template("compound-similarity-form.html", iframe = iframe, time = hora)

@app.route('/drugForm')
def drugForm():
	iframe = "/static/angularJS/iframe/demo.html"
	return render_template("compound-info-form.html", iframe = iframe)

@app.route('/targetResults', methods=['GET', 'POST'])
def targetResults():
	if request.method == 'POST':
		targets = []
		labels = []
		values = []

		targetController = TargetController(request.json['action'], request.json['compound'])
		targets = targetController.doAction()
		if (len(targets) != 0):
			arrayClasses = []
			for target in targets:
				arrayClasses.append(json.dumps(target['target_class']))
			for c in arrayClasses:
				if (c not in labels):
					labels.append(c)
			for c in labels:
				values.append(arrayClasses.count(c))

		return jsonify(status=True, message='Connection successfully', results=targets, labels=labels, values=values)
	else:
		return jsonify(status=False, message='Error request method')

@app.route('/similarityResults', methods=['GET', 'POST'])
def similarityResults():
	if request.method == 'POST':
		similarMols = []
		similarityController = SimilarityController(request.json['action'], request.json['compound'])
		similarMols = similarityController.doAction()
		return jsonify(status=True, message='Connection successfully', results=similarMols)
	else:
		return jsonify(status=False, message='Error request method')

@app.route('/drugResults', methods=['GET', 'POST'])
def drugResults():
	if request.method == 'POST':
		drugInfo = []
		drugController = DrugController(request.json['action'], request.json['compound'])
		drugInfo = drugController.doAction()
		path = 'static/images/queryMolecule/queryMolecule.png'
		img = ""
		if(os.path.isfile(path)):
			img = path
		return jsonify(status=True, message='Connection successfully', results=drugInfo, image = img)
	else:
		return jsonify(status=False, message='Error request method')


if __name__ == "__main__":
	app.run(host= '0.0.0.0', debug = True, use_reloader = True, port = 8000)