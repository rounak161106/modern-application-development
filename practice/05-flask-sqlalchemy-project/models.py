"""
models.py — Database Models (Separated from main.py)
=====================================================
Practice: Flask-SQLAlchemy Project — User-Role Management

This file demonstrates separating database models into their own
module. Instead of defining everything in main.py, the models are
imported from here — a cleaner, more professional approach.

Models:
    - User: stores user credentials
    - Role: defines available roles
    - Association: junction table for Many-to-Many (User <-> Role)

Key concept learned:
    - Separating models into their own file for better code organization
    - Using db = SQLAlchemy() without an app (initialized later with db.init_app)
"""

from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy instance without binding it to an app yet.
# It will be bound to the Flask app in main.py using db.init_app(app)
db = SQLAlchemy()

class User(db.Model):
    """User model — stores username and password with associated roles."""
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    # Many-to-Many: a user can have multiple roles, a role can be assigned to multiple users
    roles = db.relationship("Role", backref="users", secondary="association")

class Role(db.Model):
    """Role model — defines roles like 'admin', 'user', 'moderator', etc."""
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    role_name = db.Column(db.String, nullable = False)
    

class Association(db.Model):
    """Junction table for the Many-to-Many relationship between User and Role."""
    __tablename__ = "association"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))
