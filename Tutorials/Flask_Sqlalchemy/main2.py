from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///manymany.sqlite3"

db = SQLAlchemy(app)
app.app_context().push()

# ========== models for one to many relationship ===============

# Child Table (many side)
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)

# Parent Table (one side)
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    role_name = db.Column(db.String, nullable = False, unique = True)
    users = db.relationship("User", backref = "role")         #This backref = role will give the functionality to the User model to access the role attributes 
 