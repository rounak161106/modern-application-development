"""
main.py — Flask-SQLAlchemy Project: Role-Based User Management
================================================================
Practice: Building a CRUD app with separated models and Many-to-Many

This project demonstrates a more mature Flask application structure
where models are defined in a separate file (models.py) and imported.
It manages Roles and their associated Users.

Features:
    - List all roles on the home page
    - Create new roles
    - Edit existing role names
    - Delete roles
    - View all users assigned to a specific role

Key concepts learned:
    - Importing models from a separate module
    - db.init_app(app) pattern for late binding
    - Full CRUD operations on the Role model
    - Navigating Many-to-Many relationships via backref
    - PRG pattern (Post-Redirect-Get) for form submissions
"""

from flask import Flask, render_template, request, redirect
from models import *      # Import all models (User, Role, Association) and db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///manymany.sqlite3"

# Initialize the db instance (created in models.py) with this Flask app
db.init_app(app)

app.app_context().push()

# ──────────────────────────────────────────────────────────
# Controllers for Role Model
# ──────────────────────────────────────────────────────────

@app.route('/')
def all_roles():
    """Home page — displays all roles."""
    roles = Role.query.all()
    return render_template("index.html", roles = roles)

@app.route('/create_role', methods=["GET", "POST"])
def create():
    """Create a new role — shows form on GET, saves on POST."""
    if request.method == "GET":
        return render_template("create_role.html")
    role = request.form.get("role")
    new_role = Role(role_name=role)
    print(new_role.role_name)
    db.session.add(new_role)
    db.session.commit()
    return redirect('/')

@app.route('/edit_role/<int:role_id>', methods=["GET", "POST"])
def edit_role(role_id):
    """Edit an existing role's name."""
    if request.method == "POST":
        new_name = request.form.get("role")
        role = Role.query.get(role_id)
        role.role_name = new_name
        db.session.commit()
        return redirect('/')
    this_role = Role.query.get(role_id)
    return render_template("edit_role.html", this_role=this_role)

@app.route('/delete_role/<int:role_id>')
def delete_role(role_id):
    """Delete a role from the database."""
    this_role = Role.query.get(role_id)
    db.session.delete(this_role)
    db.session.commit()
    return redirect("/")

@app.route('/users/<role>')
def role_users(role):
    """View all users associated with a specific role."""
    role_obj = Role.query.get(role)
    # Access users through the backref defined in the User model's relationship
    users = role_obj.users
    return render_template("role_users.html", users= users, role_obj=role_obj)

app.run(debug=True)
