import os
# Configuration file, You need to replace the next values with the appropriate values for your configuration
# Note: 
# This file is being ignored in git, by assuming unchanged with this command
#   git update-index --assume-unchanged api/config.py
# To make git track the file again, run:
#   git update-index --no-assume-unchanged api/config.py

basedir = os.path.abspath(os.path.dirname(__file__))
DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(DB_USER="user_name", DB_PASS="user_password", DB_ADDR="127.0.0.1", DB_NAME="messages")
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
