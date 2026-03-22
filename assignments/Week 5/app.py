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
        courses = request.form.getlist("courses")
        roll_nos = [i.roll_number for i in Student.query.all()]
        if roll in roll_nos:
            return render_template("exists.html")
        new = Student(roll_number=roll, first_name=f_name, last_name=l_name)
        courses_obj = [Course.query.get(int(i[-1])) for i in courses]
        new.courses.extend(courses_obj)
        db.session.add(new)
        db.session.commit()
        return redirect('/')

@app.route('/student/<int:student_id>/update', methods=["GET", "POST"])
def update(student_id):
    this_student = Student.query.get(student_id)
    if request.method=="GET":
        return render_template("update.html", student_id=student_id, this_student=this_student)
    f_name = request.form.get("f_name")
    l_name = request.form.get("l_name")
    courses = request.form.getlist("courses")
    this_student = Student.query.get(student_id)
    this_student.first_name=f_name
    this_student.last_name=l_name
    courses_obj = [Course.query.get(int(i[-1])) for i in courses]
    this_student.courses=courses_obj
    db.session.commit()
    return redirect('/')

@app.route('/student/<int:student_id>/delete')
def delete(student_id):
    student = Student.query.get(student_id)
    enrolls = Enrollments.query.filter_by(estudent_id=student_id).all()
    print(enrolls)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')

@app.route('/student/<int:student_id>')
def show_details(student_id):
    return render_template("show_details.html", stud=Student.query.get(student_id))

if __name__ == "__main__":
    app.run(debug=True)