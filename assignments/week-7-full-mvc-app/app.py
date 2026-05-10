"""
app.py — Week 7 Assignment: Full MVC Flask Application (Students & Courses)
============================================================================
Course: Modern Application Development I (MAD-1), IIT Madras BS Program

This is the most comprehensive assignment — a complete, production-style
Flask MVC web application with a full UI for managing Students, Courses,
and their Enrollments. It combines everything learned in previous weeks:
    - Flask routing (Week 4)
    - SQLAlchemy ORM (Week 5)
    - CRUD operations (Week 5-6)
    - Jinja2 templating (Week 3-4)

Architecture: MVC (Model-View-Controller)
    - Models: Student, Course, Enrollments (defined as Python classes)
    - Views: Jinja2 HTML templates in the templates/ folder
    - Controllers: Flask route functions that handle business logic

Features:
    - Full CRUD for Students (create, read, update, delete)
    - Full CRUD for Courses (create, read, update, delete)
    - Enrollment management (enroll in a course, withdraw from a course)
    - Duplicate entry detection for roll numbers and course codes
    - Reusable error template with dynamic messages

Key concepts learned:
    - MVC architecture — clear separation of concerns
    - Many-to-Many relationships with enrollment management
    - Reusable Jinja2 templates with dynamic context variables
    - url_for() for generating URLs in templates
    - Complete web application lifecycle
"""

# ──────────────────────────────────────────────────────────
# Imports & Configuration
# ──────────────────────────────────────────────────────────
from flask import Flask,render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///week7_database.sqlite3'
db = SQLAlchemy(app)
app.app_context().push()

# ──────────────────────────────────────────────────────────
# Models (Database Layer)
# ──────────────────────────────────────────────────────────
# These models define the database schema. SQLAlchemy creates the
# tables automatically based on these class definitions.

class Student(db.Model):
    """Student model — stores student information."""
    student_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    roll_number = db.Column(db.String, unique = True, nullable = False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)

class Course(db.Model):
    """Course model — stores course information."""
    course_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    course_code = db.Column(db.String, unique = True, nullable = False)
    course_name = db.Column(db.String, nullable = False)
    course_description = db.Column(db.String)
    # Many-to-Many relationship: Course <-> Student via enrollments table
    students = db.relationship("Student", backref = "courses", secondary = "enrollments")

class Enrollments(db.Model):
    """Junction table for Many-to-Many relationship between Student and Course."""
    enrollment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    estudent_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable = False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable = False)

# ──────────────────────────────────────────────────────────
# Controllers — Student Routes
# ──────────────────────────────────────────────────────────

@app.route('/')
def home():
    """Home page — displays a list of all registered students."""
    students = Student.query.all()
    return render_template("index.html", students = students)

@app.route("/student/create", methods = ["GET", "POST"])
def addStudent():
    """
    Create a new student.
    GET:  Show the student creation form
    POST: Validate input, check for duplicate roll number, and save to database
    """
    if request.method == "GET":
        return render_template('add_student.html')
    roll = request.form.get("roll")
    fname = request.form.get("f_name")
    lname = request.form.get("l_name")
    # Check if roll number already exists in the database
    existing = Student.query.filter_by(roll_number = roll).first()
    if existing:
        return render_template('existing.html', type = "Student", todo = "use", what = "Roll Number", endpoint = "/")
    new_student = Student(roll_number = roll, first_name = fname, last_name = lname)
    db.session.add(new_student)
    db.session.commit()
    return redirect('/')

@app.route('/student/<int:student_id>/update', methods = ["GET", "POST"])
def update_student(student_id):
    """
    Update a student's details and add a new course enrollment.
    GET:  Show the update form pre-filled with current data + course dropdown
    POST: Save updated name and add selected course enrollment
    """
    this_student = Student.query.get(student_id)
    courses = Course.query.all()
    if request.method == "GET":
        return render_template('update_student.html', student = this_student, courses = courses)
    f_name = request.form.get("f_name")
    l_name = request.form.get("l_name")
    selected = request.form.get('course')
    selected_course = Course.query.get(selected)
    this_student.first_name = f_name 
    this_student.last_name = l_name 
    # Append the newly selected course to the student's course list
    this_courses = this_student.courses
    this_courses.append(selected_course)
    db.session.commit()
    return redirect('/')

@app.route("/student/<int:student_id>/delete")
def delete_student(student_id):
    """Delete a student from the database."""
    this_student = Student.query.get(student_id)
    db.session.delete(this_student)
    db.session.commit()
    return redirect('/')

@app.route('/student/<int:student_id>')
def student_info(student_id):
    """Display detailed information about a student and their enrolled courses."""
    this_student = Student.query.get(student_id)
    return render_template("student_info.html", student = this_student)

@app.route('/student/<int:student_id>/withdraw/<int:course_id>')
def update_enrollments(student_id, course_id):
    """Withdraw a student from a specific course by deleting the enrollment record."""
    current_enrollment = Enrollments.query.filter_by(estudent_id = student_id, ecourse_id = course_id).first()
    db.session.delete(current_enrollment)
    db.session.commit()
    return redirect('/')

# ──────────────────────────────────────────────────────────
# Controllers — Course Routes
# ──────────────────────────────────────────────────────────

@app.route('/courses')
def courses():
    """Display a list of all courses."""
    courses = Course.query.all()
    return render_template("courses.html", courses = courses)

@app.route('/course/create', methods = ["GET", "POST"])
def addCourse():
    """
    Create a new course.
    GET:  Show the course creation form
    POST: Validate input, check for duplicate course code, and save to database
    """
    if request.method == "GET":
        return render_template('add_course.html')
    code = request.form.get("code")
    c_name = request.form.get("c_name")
    desc = request.form.get("desc")
    # Check if course code already exists
    existing = Course.query.filter_by(course_code = code).first()
    if existing:
        return render_template('existing.html', type = "Course", todo = "create a", what = "course", endpoint = '/courses')
    new_course = Course(course_code = code, course_name = c_name, course_description = desc)
    db.session.add(new_course)
    db.session.commit()
    return redirect('/courses')

@app.route('/course/<int:course_id>/update', methods = ["GET", "POST"])
def update_course(course_id):
    """Update a course's name and description."""
    this_course = Course.query.get(course_id)
    if request.method == "GET":
        return render_template('update_course.html', course = this_course)
    c_name = request.form.get("c_name")
    desc = request.form.get("desc")
    this_course.course_name = c_name
    this_course.course_description = desc
    db.session.commit()
    return redirect('/courses')
    
@app.route("/course/<int:course_id>/delete")
def delete_course(course_id):
    """Delete a course from the database."""
    this_course = Course.query.get(course_id)
    db.session.delete(this_course)
    db.session.commit()
    return redirect('/')

@app.route('/course/<int:course_id>')
def course_info(course_id):
    """Display detailed information about a course and its enrolled students."""
    this_course = Course.query.get(course_id)
    print(this_course)
    return render_template("course_info.html", course = this_course)

# ──────────────────────────────────────────────────────────
# Run the App
# ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)