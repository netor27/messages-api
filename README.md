[![Python](https://img.shields.io/badge/python-3.5.2-blue.svg)]()
[![Requirements Status](https://requires.io/github/netor27/messages-api/requirements.svg?branch=master)](https://requires.io/github/netor27/messages-api/requirements/?branch=master)
[![Travis](https://travis-ci.org/netor27/messages-api.svg?branch=master)](https://travis-ci.org/netor27/messages-api)
[![Coverage](https://codecov.io/gh/netor27/messages-api/branch/master/graph/badge.svg)](https://codecov.io/gh/netor27/messages-api)


# messages-api
Python/Flask simple web api. This API manage the following resources:

* messages : Information about a specific message (duration, date, category, etc.)

* messageCategories: CategoryName and relationship with messages


## Requirements

* [python ^3.5.2](https://www.python.org)
* pip package manager
* [postgreSql ^9.5.10](https://www.postgresql.org/)

## Installation

* Create your virtual environment.

```
python3 -m venv ./env/messages-api
```
* Activate your virtual environment. 

```
source ./env/messages-api/bin/activate
```

* Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

* Create a database in PostgreSQL, login as the default user (set YOUR_DB_NAME to your desired new db name)
```
sudo -u postgres createdb YOUR_DB_NAME
sudo -u postgres -i
```

* Run the psql client and create a new user with a role to manage the new db. (set user_name to your user and YOUR_DB_NAME to your database name)

```
psql

CREATE ROLE user_name WITH LOGIN PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE YOUR_DB_NAME TO user_name; 
ALTER USER user_name CREATEDB;
```

* Update the contents of config.py to match the values you used to create your db and your user name.

* Initialize the db via migration
```
python3 api/migrate.py db upgrade
python3 api/migrate.py db migrate
```

## Setting up the unit test environment

* Create a database in PostgreSQL, login as the default user (set YOUR_TEST_DB_NAME to your desired new db name)
```
sudo -u postgres createdb YOUR_TEST_DB_NAME
sudo -u postgres -i
```

* Run the psql client and set the privileges to our previously created user to manage the new db. (set user_name to your user and YOUR_TEST_DB_NAME to your test database name)

```
psql

GRANT ALL PRIVILEGES ON DATABASE YOUR_TEST_DB_NAME TO user_name;
```

## Running unit tests

* Use nose2 to run the tests from the api subfolder and creating an html report

```
cd api
nose2 -v --with-coverage
coverage report -m
coverage html
```
The report for the last run is located relatively from the api folder in ./htmlcov/index.html'




## Running the API

```
source ./env/messages-api/bin/activate
python3 api/run.py
```

The API is running by default in the port 5000
