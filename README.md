# messages-api
Python/Flask simple web api. This API manage the following resources:

* messages : Information about a specific message (duration, date, category, etc.)


## Requirements

* [python ^3.5.2](https://www.python.org)
* pip package manager

## Installation

* create your virtual environment. Example with venv:
```
python3 -m venv ~/Envs/messages-api01/
```
* activate your virtual environment. Example:
```
source ~/Envs/messages-api01/bin/activate
```
* pip install -r requirements.txt

## Running the API

```
python3 api/api.py
```

## Consume the API

The API is running by default in the port 5000.
