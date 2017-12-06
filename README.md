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
python3 -m venv ~/Envs/messages-api01/
```
* Activate your virtual environment. 

```
source ~/Envs/messages-api01/bin/activate
```

* Install dependencies
```
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
python3 api/migrate.py db migrate
python3 api/migrate.py db upgrade
```

## Running the API

```
python3 api/api.py
```

## Consuming the API

The API is running by default in the port 5000.
