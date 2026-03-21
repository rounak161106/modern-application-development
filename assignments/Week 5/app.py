from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
path = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(path, "database.sqlite3")
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class Student(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String)     
    
class Course(db.Model):
    __tablename__ = "course"
    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course_code = db.Column(db.String,unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)   

class Enrollments(db.Model):
    __tablename__ = "enrollments"
    enrollment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable=False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable=False)

print(Student.student_id)
@app.route('/')
def home():
    students = Student.query.all()
    if not students:
        return render_template("no_students.html")
    else:
        return render_template("home.html", students=students)

@app.route('/student/create', methods=["GET", "POST"])
def create():
    if request.method=="GET":
        return render_template("create.html")
    
    roll = request.form.get("roll")
    f_name = request.form.get("f_name")
    l_name = request.form.get("l_name")

    print(roll)
    print(f_name )
    print(l_name )

if __name__ == "__main__":
    app.run(debug=True)