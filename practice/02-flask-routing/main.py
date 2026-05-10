"""
main.py — Flask Routing Experiments
=====================================
Practice: Experimenting with Flask URL routing rules

This file was my playground for understanding how Flask routes work.
I experimented with different URL patterns, including:
    - Double slashes in routes
    - Nested route paths
    - How Flask handles trailing slashes

This was purely experimental — I was learning how Flask's URL routing
engine parses and matches different patterns.

Key concepts learned:
    - @app.route() decorator for defining URL routes
    - Flask's URL routing engine and pattern matching
    - How host='0.0.0.0' makes the server accessible on the network
    - debug=True enables auto-reload on code changes
"""

from flask import Flask

app = Flask(__name__)

# Experimenting with double slashes in URLs
@app.route('//')
def index():
    return "this is index page"

# Simple single-path route
@app.route('/aboutpage')
def Home():
    return 'This is my home page'

# Route with trailing slash
@app.route('/projectpage/')
def projects():
    return 'The project page'

# Nested route with multiple slashes — testing Flask's URL handling
@app.route('/aboutpage/projectpage///')
def result():
    return 'This is about the project page'

if __name__ == "__main__":
    # host='0.0.0.0' makes the app accessible from other devices on the network
    app.run(host='0.0.0.0', debug=True)