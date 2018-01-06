import os
# Configuration file, You need to replace the next values with the appropriate values for your configuration
# Note: 
# This file is being ignored in git, by assuming unchanged with this command
#   git update-index --assume-unchanged api/test_config.py
# To make git track the file again, run:
#   git update-index --no-assume-unchanged api/test_config.py

# You need to replace the next values with the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="user_name", DB_PASS="password", DB_ADDR="127.0.0.1", DB_NAME="test_messages")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
TESTING = True
SERVER_NAME = '127.0.0.1:5000'
#Disable CSRF protection in the testing configuration
WTF_CSRF_ENABLED = False
