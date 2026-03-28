#<=========================================Add imports=====================================>
from flask import Flask,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

#<=======================Configurations================================>
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///week7_database.sqlite3'
db = SQLAlchemy(app)
app.app_context().push()

#<==========================================Models=======================================>
class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    roll_number = db.Column(db.String, unique = True, nullable = False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)

class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    course_code = db.Column(db.String, unique = True, nullable = False)
    course_name = db.Column(db.String, nullable = False)
    course_description = db.Column(db.String)

class Enrollments(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    estudent_id = db.Column(db.Integer, db.ForeignKey(Student.student_id), nullable = False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey(Course.course_id), nullable = False)

#<===========================================Controllers=========================================>
@app.route('/')
def home():
    return render_template("index.html")