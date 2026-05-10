"""
api_with_db.py — API with Database-Backed Data
================================================
Practice: Connecting a Flask API to a real SQLAlchemy database

This was the next step after intro.py — instead of in-memory data,
this API reads from an actual SQLite database. This means data
persists across server restarts!

The database uses a Many-to-Many relationship between User and Role
(similar to the student-course pattern from the assignments).

Key concepts learned:
    - Combining Flask routes with SQLAlchemy database queries
    - Querying with filter() and first()
    - Returning database objects as JSON dictionaries
    - Building custom JSON responses from model attributes
    - Proper 404 handling when a record isn't found
"""

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///apidb.sqlite3"

db = SQLAlchemy(app)
app.app_context().push()

# ──────────────────────────────────────────────────────────
# Models — Many-to-Many relationship: User <-> Role
# ──────────────────────────────────────────────────────────

class User(db.Model):
    """User model with name and password."""
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    roles = db.relationship("Role", backref="users", secondary="association")

class Role(db.Model):
    """Role model — roles that can be assigned to users."""
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    role_name = db.Column(db.String, nullable = False, unique = True)
    

class Association(db.Model):
    """Junction table linking users to roles (Many-to-Many)."""
    __tablename__ = "association"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))

# ──────────────────────────────────────────────────────────
# API Routes
# ──────────────────────────────────────────────────────────

@app.get('/getdata')
def get_data():
    """Retrieve all users and return their name and password as JSON."""
    users = User.query.all()
    my_data = []
    # Manually building JSON response from model objects
    for user in users:
        this_user = {}
        this_user["name"] = user.name 
        this_user["pass"] = user.password 
        my_data.append(this_user)

    return my_data

@app.get('/user/<username>')
def user(username):
    """Look up a specific user by username. Returns 404 if not found."""
    this_user = User.query.filter(User.name == username).first()
    if not this_user:
        return {"message": "not found"},404
    return {"name": this_user.name, "pass":this_user.password}

if __name__ == "__main__":
    app.run(debug=True)