from flask import Flask, request
from models import *
from flask_restful import Api

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///apidb.sqlite3"
db.init_app(app)
api = Api(app)
app.app_context().push()