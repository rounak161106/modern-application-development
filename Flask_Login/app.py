from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdb.sqlite3"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username = username).first()
        if user:
            if user.password == password:
                return redirect(f"/dashboard/{user.id}")
            else:
                return "Incorrect Password"
            
        else:
            return "User not found"
    
    return render_template("login_form.html")

@app.route('/dashboard/<int:id>')
def dashboard(id):
    user = User.query.get(id)
    return render_template("dashboard.html", user = user)

if __name__ == "__main__":
    app.run(debug=True)