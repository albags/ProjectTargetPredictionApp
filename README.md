# Target Prediction App

Application for target prediction and calcul of similarities for small molecules.  

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

* [Anaconda Python 2.7](https://www.anaconda.com/download/)
* [Flask](http://flask.pocoo.org/docs/0.12/installation/)
* [Numpy](https://scipy.org/install.html)
* [Rdkit](http://www.rdkit.org/docs/Install.html)
* [Usrcat](https://bitbucket.org/aschreyer/usrcat)
* [Electroshape](https://bitbucket.org/aschreyer/electroshape)
* [Plotly](https://plot.ly/python/getting-started/)
* [Mysql](https://dev.mysql.com/doc/refman/5.7/en/installing.html)

### Installing & running
Clone the project on your local machine

`$ git clone https://github.com/albags/ProjectTargetPredictionApp.git`

`$ cd ProjectTargetPredictionApp/`

Install database, remember to create the database first in your local mysql
`$ mysql -u username -p database_name < project_fda.sql`

Remember to change the user and the password into the [DBConnect.py](/pythonFlask/model/persist/DBConnect.py) file.

Run the application

`$ python run.py`

Go to your browser into [0.0.0.0:5000](http://0.0.0.0:8000/)

## Table of content

| 		Content  	 | 				Explanation 	 		|
| ------------------ | ------------------------------------ |
| Target Prediction  | Based in ChEMBL database bioactiviy  |
| Similarity 2D  	 | Using Fingerprint  					|
| Similarity 3D  	 | Using Usrcat and Electroshap methods |
| Molecule information  	 |  |

## Licence
ProjectTargetPredictionApp is released under the [MIT License](LICENSE).
