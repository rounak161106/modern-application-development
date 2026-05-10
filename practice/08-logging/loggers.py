"""
loggers.py — Flask Logging Tutorial
=====================================
Practice: Using Python's logging module instead of print() for debugging

This is a simple demonstration of using Flask's built-in logger
(which wraps Python's logging module) instead of print() statements.

Why use logging instead of print()?
    - Logs can be saved to a file (useful for production debugging)
    - Logs have severity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    - Logs can be filtered and formatted
    - print() output is lost when the terminal closes

Key concepts learned:
    - logging.basicConfig() to configure log file and level
    - app.logger.warning() to log messages at WARNING level
    - Log levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
    - Only messages at or above the configured level are recorded
"""

# This is a simple tutorial to use loggers instead of using print statement to debug our code

from flask import Flask, render_template
import logging

# Configure logging to write to a file called 'debug.log'
# Only messages at WARNING level or above will be recorded
logging.basicConfig(filename="debug.log", level=logging.WARNING)

app = Flask(__name__)

@app.route("/")
def index():
    """Home page — logs a warning message each time the page is accessed."""
    app.logger.warning("Index page was accessed")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)