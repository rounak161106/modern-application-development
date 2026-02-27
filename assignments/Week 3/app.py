from jinja2 import Template
import sys
import csv
import matplotlib.pyplot as plt

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
marks=[]
courses=[]
students=[]
with open("data.csv", "r") as f:
    cntinstr = f.read()
    content = cntinstr.split("\n")
    header=content[0].split(", ")
    data=[x.split(", ") for x in content[1:]]
    reader = csv.DictReader(f)
    f.seek(0)
    for row in reader:
        courses.append(row[" Course id"].strip())
        students.append(row["Student id"].strip())
        if row[" Course id"].strip()==course_id:
            marks.append(int(row[" Marks"].strip()))

plt.hist(marks, bins=10)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Marks")
plt.savefig("graph.png")
plt.close()

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
                <td>{{header[0]}}</td>
                <td>{{header[1]}}</td>
                <td>{{header[2]}}</td>
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
                <td>Average Marks</td>
                <td>Maximum Marks</td>
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


template = Template(TEMPLATE)
cnt=template.render(invalid=invalid, arg1=arg1, student_id=student_id, cntinstr=cntinstr, course_id=course_id, students=students, courses=courses, header=header, data=data)

with open("output.html", "w") as f:
    f.write(cnt)