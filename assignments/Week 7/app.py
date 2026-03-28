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
    students = db.relationship("Student", backref = "courses", secondary = "enrollments")

class Enrollments(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    estudent_id = db.Column(db.Integer, db.ForeignKey("student.student_id"), nullable = False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey("course.course_id"), nullable = False)

#<===========================================Controllers=========================================>
@app.route('/')
def home():
    students = Student.query.all()
    return render_template("index.html", students = students)

@app.route("/student/create", methods = ["GET", "POST"])
def addStudent():
    if request.method == "GET":
        return render_template('add_student.html')
    roll = request.form.get("roll")
    fname = request.form.get("f_name")
    lname = request.form.get("l_name")
    existing = Student.query.filter_by(roll_number = roll).first()
    if existing:
        return render_template('existing.html', type = "Student", todo = "use", what = "Roll Number", endpoint = "/")
    new_student = Student(roll_number = roll, first_name = fname, last_name = lname)
    db.session.add(new_student)
    db.session.commit()
    return redirect('/')

@app.route('/student/<int:student_id>/update', methods = ["GET", "POST"])
def update_student(student_id):
    this_student = Student.query.get(student_id)
    if request.method == "GET":
        return render_template('update_student.html', student = this_student)

@app.route("/student/<int:student_id>/delete")
def delete_student(student_id):
    this_student = Student.query.get(student_id)
    db.session.delete(this_student)
    db.session.commit()
    return redirect('/')

@app.route('/student/<int:student_id>')
def student_info(student_id):
    this_student = Student.query.get(student_id)
    print(this_student)
    return render_template("student_info.html", student = this_student)

@app.route('/student/<int:student_id>/withdraw/<int:course_id>')
def update_enrollments(student_id, course_id):
    current_enrollment = Enrollments.query.filter_by(estudent_id = student_id, ecourse_id = course_id).first()
    db.session.delete(current_enrollment)
    db.session.commit()
    return redirect('/')

@app.route('/courses')
def courses():
    courses = Course.query.all()
    return render_template("courses.html", courses = courses)

@app.route('/course/create', methods = ["GET", "POST"])
def addCourse():
    if request.method == "GET":
        return render_template('add_course.html')
    code = request.form.get("code")
    c_name = request.form.get("c_name")
    desc = request.form.get("desc")
    existing = Course.query.filter_by(course_code = code).first()
    if existing:
        return render_template('existing.html', type = "Course", todo = "create a", what = "course", endpoint = '/courses')
    new_course = Course(course_code = code, course_name = c_name, course_description = desc)
    db.session.add(new_course)
    db.session.commit()
    return redirect('/courses')

@app.route('/course/<int:course_id>/update', methods = ["GET", "POST"])
def update_course(course_id):
    this_course = Course.query.get(course_id)
    if request.method == "GET":
        return render_template('update_course.html', course = this_course)
    c_name = request.form.get("c_name")
    desc = request.form.get("desc")
    this_course.course_name = c_name
    this_course.course_description = desc
    db.session.commit()
    return redirect('/courses')
    
    

#<==========================================Running the app======================================>
if __name__ == "__main__":
    app.run(debug=True)