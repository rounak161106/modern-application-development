"""
app.py — Flask-Login: User Authentication System
==================================================
Practice: Implementing user authentication with Flask-Login

This was my exploration of Flask-Login — a library that manages
user sessions, login/logout, and access control for Flask apps.

Flask-Login provides:
    - login_user() — stores user info in the session (via cookies)
    - current_user — access the logged-in user in any route/template
    - @login_required — decorator to protect routes from unauthenticated access
    - logout_user() — clears the user session

Authentication Flow:
    1. User visits /login → sees the login form
    2. User submits username + password → server validates credentials
    3. If valid → login_user() stores user in session → redirect to /dashboard
    4. Dashboard reads current_user to display personalized content
    5. User clicks logout → logout_user() clears session → redirect to /login

Note: This is a learning demo — passwords are stored in plaintext.
      In production, always use werkzeug.security.generate_password_hash()!

Key concepts learned:
    - Flask-Login setup (LoginManager, user_loader)
    - UserMixin — provides default implementations for Flask-Login
    - login_user() / logout_user() for session management
    - @login_required decorator for protecting routes
    - current_user proxy for accessing the logged-in user
    - SECRET_KEY requirement for session security
"""

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user

# ──────────────────────────────────────────────────────────
# App Configuration
# ──────────────────────────────────────────────────────────
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testdb.sqlite3"
# SECRET_KEY is required for session management (encrypts the session cookie)
app.config["SECRET_KEY"] = "thisisasecretkey"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

# ──────────────────────────────────────────────────────────
# Flask-Login Setup
# ──────────────────────────────────────────────────────────
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    """
    This callback is triggered by Flask-Login to reload the user object
    from the session. When login_user(user) is called, Flask-Login stores
    the user's ID in the session cookie. On subsequent requests, this
    function uses that ID to load the full user object from the database.
    """
    return User.query.get(id)

# ──────────────────────────────────────────────────────────
# User Model
# ──────────────────────────────────────────────────────────
class User(db.Model, UserMixin):
    """
    User model — inherits from both db.Model (for database) and
    UserMixin (which provides default implementations for Flask-Login's
    required methods: is_authenticated, is_active, is_anonymous, get_id).
    """
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)

# ──────────────────────────────────────────────────────────
# Routes
# ──────────────────────────────────────────────────────────

@app.route('/')
@app.route('/login', methods = ['GET', 'POST'])
def login():
    """
    Login page — shows the login form on GET, validates credentials on POST.
    On successful login, redirects to the dashboard.
    """
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        # Look up the user in the database
        user = User.query.filter_by(username = username).first()
        if user:
            if user.password == password:
                # login_user() stores the user in the session
                login_user(user)
                # return redirect(f"/dashboard/{user.id}")
                return redirect(f"/dashboard")
            else:
                return "Incorrect Password"
            
        else:
            return "User not found"
    
    return render_template("login_form.html")

# @app.route('/dashboard/<int:id>')
@app.route('/dashboard')
@login_required    # This route requires the user to be logged in
def dashboard():
    """
    Dashboard page — only accessible to logged-in users.
    Uses current_user to access the logged-in user's data.
    """
    user = current_user    # current_user is a proxy provided by Flask-Login
    # user = User.query.get(id)
    return render_template("dashboard.html", user = user)

@app.route('/logout')
@login_required    # Can't logout if not logged in
def logout():
    """Log the user out and redirect to the login page."""
    logout_user()          # Clears the user from the session
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)