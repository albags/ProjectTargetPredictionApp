# Target Prediction App

Application for: 
* Target Prediction base in Chembl database.
* Molecule information.
* Find similarities 2D with fingerprints.
* Find similarities 3D with Usrcat and Electroshape methods.

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
* [Mysql](https://dev.mysql.com/doc/refman/5.7/en/installing.html)s

### Installing & running
Clone the project on your local machine

`$ git clone https://github.com/albags/ProjectTargetPredictionApp.git`

`$ cd ProjectTargetPredictionApp/`

Install database, remember to create the database first in your local mysql
`$ mysql -u username -p database_name < project_fda.sql`

Change _user_ and _password_ to your local ones in [DBConnect.py](pythonFlask/model/persist/DBConnect.py)
Run the application

`$ python run.py`

Go to your browser into [0.0.0.0:5000](http://0.0.0.0:8000/)


## Licence
ProjectTargetPredictionApp is released under the [MIT License](LICENSE).