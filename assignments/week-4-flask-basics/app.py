"""
app.py — Week 4 Assignment: Flask Web Application with Forms & Charts
=====================================================================
Course: Modern Application Development I (MAD-1), IIT Madras BS Program

This Flask web application:
1. Displays a form where users can select Student ID or Course ID
2. On form submission, reads data from a CSV file
3. For students: shows a table of all courses and total marks
4. For courses: shows average/max marks and a Matplotlib histogram

This was my first Flask application — the transition from CLI (Week 3)
to a web-based interface using Flask's routing and template rendering.

Usage:
    python app.py
    Then open http://localhost:5000 in your browser

Key concepts learned:
    - Flask routing with @app.route() for GET and POST methods
    - HTML form handling using request.form
    - Template rendering with render_template()
    - Serving static files from the static/ folder
    - Generating and saving charts with Matplotlib
    - Conditional routing based on form input values
"""

# ──────────────────────────────────────────────────────────
# Imports
# ──────────────────────────────────────────────────────────
from flask import Flask
from flask import render_template
from flask import request
import matplotlib
import os
matplotlib.use('Agg')       # Use non-interactive backend (no GUI window)
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────────
# Load CSV Data at Startup
# ──────────────────────────────────────────────────────────
# The CSV data is loaded once when the server starts.
# This means changes to data.csv require a server restart to take effect.
# Note: The path below assumes the script is run from the repository root.
with open("assignments/Week 4/data.csv","r") as f:
    data = f.read().strip().split("\n")[1:]          # Skip header row
    row=[i.strip().split(',') for i in data]        # Split each row by comma
    students=[i[0].strip() for i in row]            # Extract all student IDs
    courses=[i[1].strip() for i in row]             # Extract all course IDs

# ──────────────────────────────────────────────────────────
# Flask App & Routes
# ──────────────────────────────────────────────────────────
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route — handles both displaying the form (GET) and
    processing form submissions (POST).
    
    The form lets the user choose between Student ID or Course ID,
    enter an ID value, and submit. Based on the selection:
    - Student ID → renders student.html with marks table
    - Course ID → generates histogram and renders courses.html
    - Invalid input → renders error.html
    """
    if request.method=="GET":
        # Display the input form
        return render_template("index.html")
    
    elif request.method=="POST":
        # Extract form data
        selected = request.form.get("ID")            # "student_id" or "course_id"
        id_value = request.form.get("id_value")      # The actual ID entered

        # Validate that both fields are filled
        if not selected or not id_value:
            return render_template("error.html")
        
        # ── Handle Student ID queries ──
        elif request.form.get("ID")=="student_id":
            # Filter rows matching the student ID
            data=[i for i in row if i[0]==id_value]
            if request.form["id_value"] in students:
                return render_template("student.html", data=data)
            else:
                return render_template("error.html")
        
        # ── Handle Course ID queries ──
        elif request.form.get("ID")=="course_id":
            if request.form["id_value"] in courses:
                # Filter rows and extract marks for the course
                data=[i for i in row if i[1].strip()==id_value]
                marks=[int(i[2].strip()) for i in row if i[1].strip()==id_value]
                
                # Calculate max and sum manually (learning exercise)
                max=0
                sum=0
                for i in data:
                    sum+=int(i[2].strip())
                    if int(i[2].strip())>=max:
                        max=int(i[2].strip())

                # Generate histogram and save to static/ folder
                plt.hist(marks, bins=10)
                plt.xlabel("Marks")
                plt.ylabel("Frequency")
                plt.savefig(os.path.join(app.root_path, "static", "graph.png"))
                plt.close()    
                
                # Render the courses template with computed statistics
                return render_template("courses.html", avg=sum/len(data), max=max)
            else:
                return render_template("error.html")
            
    else:
        return "Something went wrong!"

# ──────────────────────────────────────────────────────────
# Run the App
# ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)