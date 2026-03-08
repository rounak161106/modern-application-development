from flask import Flask
from flask import render_template
from flask import request
import matplotlib
import os
matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open("assignments/Week 4/data.csv","r") as f:
    data = f.read().strip().split("\n")[1:]
    row=[i.strip().split(',') for i in data]
    students=[i[0].strip() for i in row]
    courses=[i[1].strip() for i in row]

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="GET":
        return render_template("index.html")
    
    elif request.method=="POST":
        selected = request.form.get("ID")
        id_value = request.form.get("id_value")
        if not selected or not id_value:
            return render_template("error.html")
        elif request.form.get("ID")=="student_id":
            data=[i for i in row if i[0]==id_value]
            if request.form["id_value"] in students:
                return render_template("student.html", data=data)
            else:
                return render_template("error.html")
        elif request.form.get("ID")=="course_id":
            if request.form["id_value"] in courses:
                data=[i for i in row if i[1].strip()==id_value]
                marks=[int(i[2].strip()) for i in row if i[1].strip()==id_value]
                max=0
                sum=0
                for i in data:
                    sum+=int(i[2].strip())
                    if int(i[2].strip())>=max:
                        max=int(i[2].strip())

                plt.hist(marks, bins=10)
                plt.xlabel("Marks")
                plt.ylabel("Frequency")
                plt.savefig(os.path.join(app.root_path, "static", "graph.png"))
                plt.close()    
                
                return render_template("courses.html", avg=sum/len(data), max=max)
            else:
                return render_template("error.html")
            
    else:
        return "Something went wrong!"

if __name__ == "__main__":
    app.run(debug=True)