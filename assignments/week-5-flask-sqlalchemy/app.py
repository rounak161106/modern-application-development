"""
app.py — Week 5 Assignment: Flask + SQLAlchemy CRUD Application
================================================================
Course: Modern Application Development I (MAD-1), IIT Madras BS Program

This application demonstrates a full CRUD (Create, Read, Update, Delete)
web application using Flask and Flask-SQLAlchemy. It manages students
and their course enrollments using an SQLite database.

This was the first time I worked with an ORM (Object-Relational Mapper)
instead of raw CSV files. The key learning was understanding how Python
classes map to database tables, and how relationships between tables
work through SQLAlchemy.

Features:
    - List all students on the home page
    - Create a new student with course selection
    - Update student details and course enrollments
    - Delete a student record
    - View detailed student information with enrolled courses

Database:
    - SQLite database auto-created in the instance/ folder
    - Three tables: student, course, enrollments (junction table)
    - Many-to-Many relationship between Student and Course

Key concepts learned:
    - Flask-SQLAlchemy ORM setup and configuration
    - Defining database models as Python classes
    - Many-to-Many relationships using a junction/association table
    - CRUD operations (add, query, update, delete)
    - The PRG (Post-Redirect-Get) pattern to prevent duplicate form submissions
    - db.relationship() with secondary parameter for M2M
"""

# ──────────────────────────────────────────────────────────
# Imports & Configuration
# ──────────────────────────────────────────────────────────
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# SQLite database will be stored in the instance/ folder (auto-created by Flask)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

# ──────────────────────────────────────────────────────────
# Database Models
# ──────────────────────────────────────────────────────────
# Each class below maps to a table in the SQLite database.
# SQLAlchemy automatically creates the tables based on these definitions.

class Student(db.Model):
    """Represents a student in the system."""
    __tablename__ = "student"
    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    roll_number = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String) 
    # Many-to-Many relationship: a student can enroll in many courses,
    # and a course can have many students. The 'secondary' parameter
    # tells SQLAlchemy to use the 'enrollments' table as the junction table.
    courses = db.relationship("Course", backref="students", secondary="enrollments")    
    
class Course(db.Model):
    """Represents a course that students can enroll in."""
    __tablename__ = "course"
    course_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course_code = db.Column(db.String,unique=True, nullable=False)
    course_name = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String)   

class Enrollments(db.Model):
    """
    Junction table for the Many-to-Many relationship between Student and Course.
    Each row represents one enrollment — linking a student to a course.
    """
    __tablename__ = "enrollments"
    enrollment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    estudent_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable=False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable=False)

# ──────────────────────────────────────────────────────────
# Routes (Controllers)
# ──────────────────────────────────────────────────────────

print(Student.student_id)

@app.route('/')
def home():
    """Home page — displays a list of all students."""
    students = Student.query.all()
    return render_template("home.html", students=students)

@app.route('/student/create', methods=["GET", "POST"])
def create():
    """
    Create a new student.
    GET: Show the creation form
    POST: Process the form data, check for duplicate roll numbers,
          and save the new student with selected courses to the database.
    """
    if request.method=="GET":
        return render_template("create.html")
    if request.method=="POST":
        roll = request.form.get("roll")
        f_name = request.form.get("f_name")
        l_name = request.form.get("l_name")
        # getlist() retrieves multiple selected values (checkboxes)
        courses = request.form.getlist("courses")
        
        # Check for duplicate roll numbers before creating
        roll_nos = [i.roll_number for i in Student.query.all()]
        if roll in roll_nos:
            return render_template("exists.html")
        
        # Create the student and associate selected courses
        new = Student(roll_number=roll, first_name=f_name, last_name=l_name)
        courses_obj = [Course.query.get(int(i[-1])) for i in courses]
        new.courses.extend(courses_obj)
        db.session.add(new)
        db.session.commit()
        # PRG pattern: redirect after POST to prevent duplicate submissions
        return redirect('/')

@app.route('/student/<int:student_id>/update', methods=["GET", "POST"])
def update(student_id):
    """
    Update an existing student's details and course enrollments.
    GET: Show the update form pre-filled with current data
    POST: Save the updated data to the database
    """
    this_student = Student.query.get(student_id)
    enrolls_obj = this_student.courses
    enrolls = [i.course_id for i in enrolls_obj]
    if request.method=="GET":
        return render_template("update.html", student_id=student_id, this_student=this_student, enrolls=enrolls)
    f_name = request.form.get("f_name")
    l_name = request.form.get("l_name")
    courses = request.form.getlist("courses")
    this_student = Student.query.get(student_id)
    this_student.first_name=f_name
    this_student.last_name=l_name
    courses_obj = [Course.query.get(int(i[-1])) for i in courses]
    # Replacing the entire courses list updates the enrollments table automatically
    this_student.courses=courses_obj
    db.session.commit()
    return redirect('/')

@app.route('/student/<int:student_id>/delete')
def delete(student_id):
    """Delete a student and their enrollment records from the database."""
    student = Student.query.get(student_id)
    enrolls = Enrollments.query.filter_by(estudent_id=student_id).all()
    print(enrolls)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')

@app.route('/student/<int:student_id>')
def show_details(student_id):
    """Show detailed information about a student and their enrolled courses."""
    return render_template("show_details.html", stud=Student.query.get(student_id))

# ──────────────────────────────────────────────────────────
# Run the App
# ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)