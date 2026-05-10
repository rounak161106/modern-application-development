"""
app.py — Tutorial: Sessions and Cookies in Flask
==================================================
Tutorial: Code written during live course tutorial sessions

This file demonstrates Flask's session management — how to store
user data in server-side sessions (backed by cookies) without
using a database or Flask-Login.

Session Flow:
    1. User visits /login → sees login form
    2. User submits credentials → stored in session dictionary
    3. User visits /dashboard → reads username from session
    4. User visits /logout → session data is cleared

This was a precursor to learning Flask-Login — understanding how
sessions work at a lower level before using a library that abstracts it.

Key concepts learned:
    - Flask session object — server-side storage backed by signed cookies
    - SECRET_KEY — required for signing/encrypting session cookies
    - session["key"] = value — store data in the session
    - session.get("key") — safely read from session (returns None if missing)
    - session.pop("key", None) — remove data from the session
"""

from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
# SECRET_KEY is required — it signs the session cookie to prevent tampering
app.config["SECRET_KEY"] = "thisisasecretkey"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    """Login route — stores credentials in the session on POST."""
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        # loading user credentials into the session 
        session["username"] = username
        session["password"] = password
        return redirect("/dashboard")
    
    return render_template("login_form.html")

@app.route('/dashboard')
def dashboard():
    """Dashboard — reads the username from the session."""
    username = session.get("username")
    return f"Welcome {username}!"

@app.route('/logout')
def logout():
    """Logout — removes user data from the session."""
    session.pop("username", None)    # Safely remove (no error if key doesn't exist)
    session.pop("password", None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)
