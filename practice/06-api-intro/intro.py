"""
intro.py — First API Practice
================================
Practice: Understanding REST APIs — GET and POST with Flask

This was my first experiment building an API (as opposed to a web app
with HTML templates). The data is stored in-memory as a Python list,
so it's NOT persistent — data is lost when the server restarts.

This helped me understand:
    - The difference between serving HTML pages vs JSON data
    - How browsers can only send GET requests (for API testing, you
      need tools like Postman, Thunder Client, or curl)
    - How POST requests add data to the server
    - HTTP status codes (200 OK, 201 Created, 404 Not Found)

Key concepts learned:
    - Returning dictionaries from Flask routes → auto-converted to JSON
    - request.json to parse JSON body from POST requests
    - Custom HTTP status codes as the second return value
    - Dynamic URL parameters with <name>
    - In-memory data is not persistent across server restarts
"""

from flask import Flask ,request
app = Flask(__name__)

# ──────────────────────────────────────────────────────────
# In-Memory Data Store
# ──────────────────────────────────────────────────────────
# This data exists only while the server is running.
# Restarting the server resets it to the original values.
data = [
    {"name":"Rounak", "age":18, "marks":90},
    {"name":"Aditya", "age":19, "marks":89},
    {"name":"Chirag", "age":19, "marks":67},
]

# ──────────────────────────────────────────────────────────
# GET Endpoints
# ──────────────────────────────────────────────────────────

@app.route('/get_data')
def get_data():
    """Return all student data as JSON."""
    return data

@app.route('/student/<name>')
def get_name(name):
    """
    Look up a student by name using a URL parameter.
    Example: /student/Rounak → returns Rounak's data
    If not found, returns a 404 error with a message.
    """
    print(request.args.get("name"))
    for i in data:
        if i.get("name") == name:
            return i                                   #sends the response with 200 ok status code
    return {"message": "Student data not found"}, 404  #sends the response with a 404 status code

# The browser provides us a medium only for get method in case of api calls and what about post?? ==> for that we use interfaces like thunderclient, postman(UI) or curl(CLI)

# ──────────────────────────────────────────────────────────
# POST Endpoints
# ──────────────────────────────────────────────────────────

#post methods usage
@app.route('/add', methods=['POST'])   #or we can write @app.post('/add') - only some syntax change
def add_name():
    """
    Add a new student via POST request with a JSON body.
    The data is added to the in-memory list (NOT persistent).
    Returns 201 status code indicating successful creation.
    """
    new_name = request.json
    data.append(new_name)
    return {"message":"Student added successfully"}, 201    #sends the response with 201 status code meaning post is successful and new data is added but the data added is not persistent and will only be added till that server is running



app.run(debug=True)
