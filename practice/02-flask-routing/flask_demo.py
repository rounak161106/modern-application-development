"""
flask_demo.py — First Flask App with Form Handling
====================================================
Practice: Learning Flask basics — routing, templates, and form handling

This was my first Flask app that handles user input! It demonstrates:
1. A GET route that shows an HTML form (index.html)
2. A POST route that receives form data and displays it (display_details.html)

This is the basic Flask request-response cycle:
    Browser → GET /     → Server returns index.html (form)
    Browser → POST /    → Server reads form data → returns display_details.html

Key concepts learned:
    - Flask app creation with Flask(__name__)
    - @app.route() decorator with methods parameter
    - request.form["key"] to access submitted form data
    - render_template() to render Jinja2 HTML templates
    - Handling GET vs POST in the same route
"""

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello_world():
    """
    Main route — shows the form on GET, processes form data on POST.
    Reads the 'name' field from the submitted form and passes it
    to the display_details.html template.
    """
    if request.method == "GET":
        return render_template('./index.html')
    
    elif request.method == "POST":
        # request.form["name"] retrieves the value of the input field named "name"
        user_name = request.form["name"]
        return render_template('display_details.html', name=user_name)
    
    else:
        print("Something went wrong")

if __name__ == '__main__':
    app.run(debug=True)