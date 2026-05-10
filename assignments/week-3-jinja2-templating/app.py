"""
app.py — Week 3 Assignment: Jinja2 Templating & CLI Data Renderer
==================================================================
Course: Modern Application Development I (MAD-1), IIT Madras BS Program

This is a command-line Python application that:
1. Accepts a flag (-s for student, -c for course) and an ID via sys.argv
2. Reads student marks data from a CSV file
3. Dynamically generates an HTML report using Jinja2 templating
4. For course queries, also generates a histogram chart using Matplotlib

Usage:
    python app.py -s 1001    → Generates HTML report for student 1001
    python app.py -c 2001    → Generates HTML report + histogram for course 2001

Key concepts learned:
    - Command-line argument parsing with sys.argv
    - CSV file reading and manual parsing
    - Jinja2 Template class for rendering dynamic HTML
    - Jinja2 namespace() for mutable variables inside loops
    - Matplotlib histogram generation (non-GUI mode with 'Agg' backend)
    - Writing generated HTML to a file from Python
"""

# ──────────────────────────────────────────────────────────
# Imports
# ──────────────────────────────────────────────────────────
from jinja2 import Template
import sys
import csv
import matplotlib
matplotlib.use('Agg')       # Use non-interactive backend (no GUI window needed)
import matplotlib.pyplot as plt

# ──────────────────────────────────────────────────────────
# Parse Command-Line Arguments
# ──────────────────────────────────────────────────────────
# sys.argv[1] = flag (-s for student, -c for course)
# sys.argv[2] = the ID value to look up
invalid="not invalid"
student_id="none"
course_id="none"
arg1 = sys.argv[1]
if arg1 == "-s":
    student_id = sys.argv[2]
elif arg1 == "-c":
    course_id = sys.argv[2]
else:
    invalid = "invalid"

# ──────────────────────────────────────────────────────────
# Read and Parse CSV Data
# ──────────────────────────────────────────────────────────
# The CSV has columns: Student id, Course id, Marks
# We read the file twice:
#   1. Manual parsing with f.read() to get raw data as lists
#   2. csv.DictReader for dictionary-based access
# This was a learning exercise — in practice, one method is sufficient.
marks=[]
courses=[]
students=[]
with open("data.csv", "r") as f:
    # First read: manual parsing to get header and data as nested lists
    cntinstr = f.read()
    content = cntinstr.split("\n")
    header=content[0].split(", ")
    data=[[col.strip() for col in x.split(", ")] for x in content[1:] if x.strip()]
    
    # Second read: using csv.DictReader for structured access
    # f.seek(0) resets file pointer to beginning after the first read
    reader = csv.DictReader(f)
    f.seek(0)
    for row in reader:
        courses.append(row[" Course id"].strip())
        students.append(row["Student id"].strip())
        # Collect marks for the requested course (used for histogram)
        if row[" Course id"].strip()==course_id:
            marks.append(int(row[" Marks"].strip()))

# ──────────────────────────────────────────────────────────
# Generate Histogram (for course queries only)
# ──────────────────────────────────────────────────────────
# If a valid course ID was provided, create a marks distribution histogram
if arg1=="-c" and course_id in courses:
    plt.hist(marks, bins=10)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.title("Distribution of Marks")
    plt.savefig("graph.png")     # Save chart as an image file
    plt.close()                  # Close the figure to free memory

# ──────────────────────────────────────────────────────────
# Jinja2 HTML Template (embedded as a Python string)
# ──────────────────────────────────────────────────────────
# This template handles three cases:
#   1. Valid student ID → shows a table of courses and marks with total
#   2. Valid course ID → shows average/max marks and the histogram image
#   3. Invalid input → shows an error message
#
# Key Jinja2 features used:
#   - {% set ns = namespace(total=0) %} → mutable variable inside a for loop
#     (regular Jinja2 variables are scoped and can't be modified inside loops)
#   - {{ value|int }} → Jinja2 filter to convert string to integer
#   - {% if %}, {% elif %}, {% else %} → conditional rendering
#   - {% for %} → looping over data
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% if invalid=="invalid" %}Something Went Wrong{%elif arg1=="-s" and student_id not in students or arg1=="-c" and course_id not in courses%}Something Went Wrong{% elif arg1=="-c"%}Course Data{%else%}Student Data{% endif %}</title>
</head>
<body>
    {%if arg1=="-s" and student_id in students -%}
        <h1>Student Details</h1>
        <table border="2">
            <tr>
                <th>{{header[0]}}</td>
                <th>{{header[1]}}</td>
                <th>{{header[2]}}</td>
            </tr>
            {% set ns = namespace(total=0) %}
            {% for d in data -%}
                {% if d[0]==student_id %}
                {% set ns.total = ns.total + d[2]|int %}
                <tr>
                    <td>{{d[0]}}</td>
                    <td>{{d[1]}}</td>
                    <td>{{d[2]}}</td>
                </tr>
                {% endif %}
            {%- endfor %}
            <tr>
                <td colspan="2">Total Marks</td>
                <td>{{ns.total}}</td>
            </tr>
        </table>
    
    {% elif arg1=="-c" and course_id in courses -%}
        <h1>Course Details</h1>{%set ns = namespace(max=0)%}{%set ns3 = namespace(ctr=0)%}{%set ns2 = namespace(total=0)%}{%for d in data -%}{% if d[1]|int==course_id|int -%}{% set ns2.total = ns2.total + d[2]|int %}{% set ns3.ctr = ns3.ctr + 1 %}{%if (d[2]|int > ns.max)%}{%set ns.max=d[2]|int%}{%endif -%}{%endif -%}{%endfor -%}
        <table border="2">
            <tr>
                <th>Average Marks</td>
                <th>Maximum Marks</td>
            </tr>
            <tr>
                <td>{{ns2.total/ns3.ctr}}</td>
                <td>{{ns.max}}</td>
            </tr>
        </table><br>
        <img src="graph.png" alt="course_graph" height="350px">

    {%else -%}
        <h1>Wrong Inputs</h1>
        <p>Something went wrong</p>
    {%endif%}
</body>
</html>
"""

# ──────────────────────────────────────────────────────────
# Render Template and Write Output
# ──────────────────────────────────────────────────────────
# Pass all variables to the Jinja2 template for rendering
template = Template(TEMPLATE)
cnt=template.render(invalid=invalid, arg1=arg1, student_id=student_id, cntinstr=cntinstr, course_id=course_id, students=students, courses=courses, header=header, data=data)

# Write the rendered HTML to output.html
with open("output.html", "w") as f:
    f.write(cnt)