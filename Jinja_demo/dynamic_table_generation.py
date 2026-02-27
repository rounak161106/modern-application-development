from jinja2 import Template

student_data = [{"id": "123", "name": "Rounak", "marks":100},
                {"id": "124", "name": "Akash", "marks":98},
                {"id": "125", "name": "Anshika", "marks":78},
                {"id": "126", "name": "Rahul", "marks":98},
                {"id": "127", "name": "Akash", "marks":55}]

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

TEMPLATE = Template(template)
index = TEMPLATE.render(student_data=student_data) 

with open("./Jinja_demo/index.html", "w") as f:
    f.write(index)