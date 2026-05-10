"""
main.py — Tutorial: One-to-Many Relationship with Flask-SQLAlchemy
===================================================================
Tutorial: Code written during live course tutorial sessions

This file demonstrates a One-to-Many relationship between Role and User:
    - One Role can have many Users
    - Each User belongs to one Role (via foreign key)

The key concept is db.relationship() with backref:
    - Defined on the "one" side (Role model)
    - 'backref="role"' gives the User model a .role attribute
      to access its parent Role object without an explicit query

One-to-Many vs Many-to-Many:
    - One-to-Many: Foreign key is on the "many" side (User has role_id)
    - Many-to-Many: Uses a junction/association table (no FK on either side)

Key concepts learned:
    - ForeignKey on the child/many side
    - db.relationship() on the parent/one side
    - backref for bidirectional access
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///onemany.sqlite3"

db = SQLAlchemy(app)
app.app_context().push()

# ========== models for one to many relationship ===============

# Child Table (many side) — each User belongs to one Role
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    # Foreign key pointing to the Role table (the "one" side)
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))

# Parent Table (one side) — one Role can have many Users
class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    role_name = db.Column(db.String, nullable = False, unique = True)
    # This relationship + backref gives both sides access:
    # Role.users → list of User objects with this role
    # User.role  → the Role object this user belongs to
    users = db.relationship("User", backref = "role")         #This backref = role will give the functionality to the User model to access the role attributes 
