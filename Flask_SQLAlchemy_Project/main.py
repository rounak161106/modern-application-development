from flask import Flask, render_template, request, redirect
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///manymany.sqlite3"

db.init_app(app)

app.app_context().push()
# Controllers for Role model
@app.route('/')
def all_roles():
    roles = Role.query.all()
    return render_template("index.html", roles = roles)

#create role controller
@app.route('/create_role', methods=["GET", "POST"])
def create():
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
    this_role = Role.query.get(role_id)
    db.session.delete(this_role)
    db.session.commit()
    return redirect("/")

@app.route('/users/<role>')
def role_users(role):
    role_obj = Role.query.get(role)
    users = role_obj.users
    return render_template("role_users.html", users= users, role_obj=role_obj)

app.run(debug=True)
