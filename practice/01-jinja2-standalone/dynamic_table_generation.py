"""
dynamic_table_generation.py — Standalone Jinja2 Demo
=====================================================
Practice: Learning Jinja2 templating outside of Flask

This was one of my first experiments with Jinja2 — generating an HTML
file from Python data WITHOUT using Flask. The script:
1. Defines student data as a list of dictionaries
2. Creates a Jinja2 template with a for loop
3. Renders the template with the data
4. Writes the result to an HTML file

This helped me understand that Jinja2 is a standalone templating engine
that can be used independently — Flask just happens to use it for
rendering templates, but it's not tied to Flask at all.

Key concepts learned:
    - Jinja2 Template class for standalone rendering
    - {% for %} loops in Jinja2
    - {{ variable }} syntax for outputting values
    - Template.render() to produce final HTML
    - Writing generated content to a file
"""

from jinja2 import Template

# ──────────────────────────────────────────────────────────
# Sample Data — list of student dictionaries
# ──────────────────────────────────────────────────────────
student_data = [{"id": "123", "name": "Rounak", "marks":100},
                {"id": "124", "name": "Akash", "marks":98},
                {"id": "125", "name": "Anshika", "marks":78},
                {"id": "126", "name": "Rahul", "marks":98},
                {"id": "127", "name": "Akash", "marks":55}]

# ──────────────────────────────────────────────────────────
# Jinja2 Template — embedded as a multi-line string
# ──────────────────────────────────────────────────────────
# The template uses {% for %} to iterate over student_data
# and {{ data["key"] }} to access dictionary values
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DocuJinja Demo</title>
</head>
<body>
    <h1>Dynamic Table Generation</h1>
    <table border="2" cellpadding="8">
        <tr>
            <td>ID</td>
            <td>Name</td>
            <td>Marks</td>
        </tr>
        {% for data in student_data %}
        <tr>
            <td>{{data["id"]}}</td>
            <td>{{data["name"]}}</td>
            <td>{{data["marks"]}}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# ──────────────────────────────────────────────────────────
# Render and Write Output
# ──────────────────────────────────────────────────────────
# Create a Template object, render it with data, and save to file
TEMPLATE = Template(template)
index = TEMPLATE.render(student_data=student_data) 

with open("./Jinja_demo/index.html", "w") as f:
    f.write(index)