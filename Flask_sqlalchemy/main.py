from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

import os
path = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(path, "testdb.sqlite3")
db = SQLAlchemy()
db.init_app(app)
app.context().push()


