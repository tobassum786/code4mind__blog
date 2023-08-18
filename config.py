from os import path, environ
from datetime import timedelta
from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config():
	FLASK_DEBUG = True
	TESTING = True

	SECRET_KEY=environ.get("SECRET_KEY")
	SQLALCHEMY_DATABASE_URI=environ.get("SQLALCHEMY_DATABASE_URI")
	SQLALCHEMY_TRACK_MODIFICATION=False

	UPLOAD_DIR=os.path.join(basedir, 'upload')


	# # session permanent
	# PERMANENT_SESSION_LIFETIME=environ.get("PERMANENT_SESSION_LIFETIME")



class DevelopmentConfig(Config):
	FLASK_DEBUG = True
	TESTING = True

	SECRET_KEY=environ.get("SECRET_KEY")
	SQLALCHEMY_DATABASE_URI=environ.get("SQLALCHEMY_DATABASE_URI")
	SQLALCHEMY_TRACK_MODIFICATION=False

	UPLOAD_DIR=os.path.join(basedir, 'upload')


	# # session permanent
	# PERMANENT_SESSION_LIFETIME=environ.get("PERMANENT_SESSION_LIFETIME")