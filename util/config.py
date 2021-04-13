import flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import environ

DEV_DB = 'postgresql://aslesusr:1234@localhost/SignLanguagePR'

app = flask.Flask(__name__)
app.secret_key = "asles"

if 'DATABASE_URL' in environ:
    app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB


db = SQLAlchemy(app)
CORS(app)