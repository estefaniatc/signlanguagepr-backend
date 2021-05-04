import flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

DEV_DB = 'postgresql://oznwwrrmbzaouj:c3734637920c26912d7cebad22d33eb971c8925425c4f2bf342d326bd1d4cb1a@ec2-3-211-37-117.compute-1.amazonaws.com:5432/d2cm180srol83l'

app = flask.Flask(__name__)
app.secret_key = "asles"

if 'DATABASE_URL' in os.environ:
    uri = os.getenv("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB


db = SQLAlchemy(app)
CORS(app)