from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class Student(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String) 
    courses = db.relationship("Course", backref="students", secondary="enrollments")    
    
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
    return render_template("home.html", students=students)

@app.route('/student/create', methods=["GET", "POST"])
def create():
    if request.method=="GET":
        return render_template("create.html")
    if request.method=="POST":
        roll = request.form.get("roll")
        f_name = request.form.get("f_name")
        l_name = request.form.get("l_name")
        

if __name__ == "__main__":
    app.run(debug=True)