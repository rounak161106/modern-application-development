from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///apidb.sqlite3"

db = SQLAlchemy(app)
app.app_context().push()

# ========== models for many to many relationship ===============

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    roles = db.relationship("Role", backref="users", secondary="association")

class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    role_name = db.Column(db.String, nullable = False, unique = True)
    

class Association(db.Model):
    __tablename__ = "association"
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))

@app.get('/getdata')
def get_data():
    users = User.query.all()
    my_data = []
    for user in users:
        this_user = {}
        this_user["name"] = user.name 
        this_user["pass"] = user.password 
        my_data.append(this_user)

    return my_data

if __name__ == "__main__":
    app.run(debug=True)