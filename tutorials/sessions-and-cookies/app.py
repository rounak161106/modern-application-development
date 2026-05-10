from flask import Flask, request, render_template, redirect, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisasecretkey"

@app.route('/login', methods = ['GET', 'POST'])
def login():
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
    username = session.get("username")
    return f"Welcome {username}!"

@app.route('/logout')
def logout():
    session.pop("username", None)
    session.pop("password", None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)

