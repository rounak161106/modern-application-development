"""
main2.py — Tutorial: Many-to-Many Relationship with Flask-SQLAlchemy
=====================================================================
Tutorial: Code written during live course tutorial sessions

This file demonstrates a Many-to-Many relationship between User and Role:
    - A User can have multiple Roles
    - A Role can be assigned to multiple Users
    - The junction table (Association) links them

The key difference from main.py (One-to-Many):
    - No ForeignKey on either User or Role
    - Instead, a separate Association table holds the FK pairs
    - db.relationship() uses the 'secondary' parameter to point to the junction table

Key concepts learned:
    - Many-to-Many relationships using a junction/association table
    - secondary parameter in db.relationship()
    - backref for bidirectional access through the junction table
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///manymany.sqlite3"

db = SQLAlchemy(app)
app.app_context().push()

# ========== models for many to many relationship ===============

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    # Many-to-Many: secondary="association" tells SQLAlchemy to use the Association table
    roles = db.relationship("Role", backref="users", secondary="association")

class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    role_name = db.Column(db.String, nullable = False, unique = True)
    

class Association(db.Model):
    """Junction table — links Users to Roles for Many-to-Many relationship."""
    __tablename__ = "association"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
