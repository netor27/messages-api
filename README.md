[![Python](https://img.shields.io/badge/python-3.5.2-blue.svg)]()
[![Requirements Status](https://requires.io/github/netor27/messages-api/requirements.svg?branch=master)](https://requires.io/github/netor27/messages-api/requirements/?branch=master)
[![Travis](https://travis-ci.org/netor27/messages-api.svg?branch=master)](https://travis-ci.org/netor27/messages-api)
[![Coverage](https://codecov.io/gh/netor27/messages-api/branch/master/graph/badge.svg)](https://codecov.io/gh/netor27/messages-api)


# messages-api
Python/Flask simple web api. This API manage the following resources:

* messages : Information about a specific message (duration, date, category, etc.)

* messageCategories: CategoryName and relationship with messages


## Start the service with docker

Install [docker](https://docs.docker.com/engine/installation/) and run:

```shell
docker-compose up
# docker-compose stop
```

Visit [http://localhost:5000](http://localhost:5000)

## Start the standalone service

### Setup the PostgreSQL database

* Create a database in PostgreSQL, login as the default user (set messages to your desired new db name)
```shell
sudo -u postgres createdb messages
sudo -u postgres -i
```
* Run the psql client and create a new user with a role to manage the new db. (set 'apiuser' to your user, 'password' to your password and 'messages' to your database name)

```
psql

CREATE ROLE apiuser WITH LOGIN PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE messages TO apiuser; 
ALTER USER apiuser CREATEDB;
```

## Setting up the database schema

* Update the contents of config.py to match the values you used to create your db and your user name.

* Initialize the db via migration
```
python3 api/migrate.py db upgrade
python3 api/migrate.py db migrate
```

### Running the service
* Install the requirements and runn the app

```shell
pip install -r requirements.txt
python app.py
```
Visit [http://localhost:5000](http://localhost:5000)

## Tests

### Running tests inside a docker container

After making changes, rebuild the docker images and run the app:

```shell
docker-compose build
docker-compose run -p 5000:5000 web python app.py
```

### Running tests with the standalone service

#### Setting up the test database

* Create a database in PostgreSQL, login as the default user (set 'test_mesages' to your desired new db name)
```
sudo -u postgres createdb 'test_messages'
sudo -u postgres -i
```

* Run the psql client and set the privileges to our previously created user to manage the new db. 

```
psql

GRANT ALL PRIVILEGES ON DATABASE test_messages TO apiuser;
```

### Running unit tests

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
