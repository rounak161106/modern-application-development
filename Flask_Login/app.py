from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        return redirect("/dashboard")
    
    return render_template("login_form.html")

@app.route('/dashboard')
def dashboard():
    return "Login Successful!"

if __name__ == "__main__":
    app.run(debug=True)