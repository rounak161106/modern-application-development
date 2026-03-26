#<=============================Required imports==============================================>
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, marshal_with, fields
from flask_cors import CORS
import json
from werkzeug.exceptions import HTTPException    #to handle exceptions

class NotFoundError(HTTPException):
    def __init__(self, status_code, type):
        self.response = make_response(f'{type} not found', status_code)
class InternalServerError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('Internal Server Error', status_code)
class ExistingError(HTTPException):
    def __init__(self, status_code, type):
        self.response = make_response(f'{type} already exist', status_code)
class EmptyError(HTTPException):
    def __init__(self, status_code, error_code, error_message):
        message = {"error_code" : error_code, "error_message" : error_message}
        self.response = make_response(json.dumps(message), status_code)
class UniqueError(HTTPException):
    def __init__(self, status_code, type):
        self.response = make_response(f'{type} already exist', status_code)
        

#<====================Configuration and setup================================================>
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api_database.sqlite3"
app.app_context().push()
db = SQLAlchemy(app)
api = Api(app)
CORS(app)

#<==========================defining models for the app=======================================>
class Course(db.Model):
    course_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    course_name = db.Column(db.String, nullable = False)
    course_code = db.Column(db.String, nullable = False, unique = True)
    course_description = db.Column(db.String)
    students = db.relationship("Student", secondary="enrollment", backref="courses")

class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    roll_number = db.Column(db.String, nullable = False, unique = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)


class Enrollment(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    student_id = db.Column(db.Integer, db.ForeignKey(Student.student_id),nullable = False)
    course_id = db.Column(db.Integer, db.ForeignKey(Course.course_id),nullable = False)

#<===========================Apis handling=================================================>

#<===========================Handling Course related requests===========================================>
course_output_fields = {
    "course_id": fields.Integer,
    "course_name": fields.String,
    "course_code": fields.String,
    "course_description": fields.String
}

class CourseApi(Resource):
    @marshal_with(course_output_fields)
    def get(self, course_id):
        course_obj = Course.query.get(course_id)
        if course_obj:
            return course_obj, 200
        elif not course_obj :
            raise NotFoundError(type="Course",status_code=404)
        else:
            raise InternalServerError(status_code=500)
        
    @marshal_with(course_output_fields)
    def post(self):
        data = request.json
        course_code_list = Course.query.all()
        course_codes = [i.course_code for i in course_code_list]
        if not data["course_code"]:
            raise EmptyError(status_code=400, error_code="COURSE002", error_message="Course Code is required")
        
        if not data["course_name"]:
            raise EmptyError(status_code=400, error_code="COURSE001", error_message="Course Name is required")
        
        if data["course_code"] in course_codes:
            raise ExistingError(status_code=409, type="course_code")
        
        if data["course_code"] not in course_codes:
            new_course = Course(course_code = data["course_code"], course_name = data["course_name"], course_description = data["course_description"])
            db.session.add(new_course)
            db.session.commit()
            return new_course, 201
        else:
            raise InternalServerError(status_code=500)

    @marshal_with(course_output_fields)
    def put(self, course_id):
        data = request.json
        existing = Course.query.filter(Course.course_id == course_id).first()
        if not data["course_code"]:
            raise EmptyError(status_code=400, error_code="COURSE002", error_message="Course Code is required")
        
        if not data["course_name"]:
            raise EmptyError(status_code=400, error_code="COURSE001", error_message="Course Name is required")
        if existing:
            course_code_existing = Course.query.filter(Course.course_code == data["course_code"]).first()
            if course_code_existing:
                raise UniqueError(type="course_id", status_code=400)
            existing.course_name = data["course_name"]
            existing.course_code = data["course_code"]
            existing.course_description = data["course_description"]
            db.session.commit()
            return existing, 200
        elif not existing:
            raise NotFoundError(type="Course",status_code=404)
        else:
            raise InternalServerError(status_code=500)

    
    def delete(self, course_id):
        existing = Course.query.filter(Course.course_id == course_id).first()
        if existing:
            db.session.delete(existing)
            db.session.commit()
            return "Successfully Deleted", 200
        elif not existing:
            raise NotFoundError(type="Course",status_code=404)
        else:
            raise InternalServerError(status_code=500)
        
# <===========================Handling Students related requests============================================>
student_output_fields = {
    "student_id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "roll_number": fields.String
}

class StudentApi(Resource):
    @marshal_with(student_output_fields)
    def get(self, student_id):
        student_obj = Student.query.get(student_id)
        if student_obj:
            return student_obj, 200
        elif not student_obj :
            raise NotFoundError(type = "Student", status_code=404)
        else:
            raise InternalServerError(status_code=500)
        
    @marshal_with(student_output_fields)
    def post(self):
        data = request.json
        student_code_list = Student.query.all()
        student_codes = [i.roll_number for i in student_code_list]
        if not data["roll_number"]:
            raise EmptyError(status_code=400, error_code="STUDENT001", error_message="Roll Number required")
        
        if not data["first_name"]:
            raise EmptyError(status_code=400, error_code="STUDENT002", error_message="First Name is required")
        
        if data["roll_number"] in student_codes:
            raise ExistingError(status_code=409, type="Student")
        
        if data["roll_number"] not in student_codes:
            new_student = Student(roll_number = data["roll_number"], first_name = data["first_name"], last_name = data["last_name"])
            db.session.add(new_student)
            db.session.commit()
            return new_student, 201
        else:
            raise InternalServerError(status_code=500)

    @marshal_with(student_output_fields)
    def put(self, student_id):
        data = request.json
        existing = Student.query.filter(Student.student_id == student_id).first()
        if not data["first_name"]:
            raise EmptyError(status_code=400, error_code="STUDENT002", error_message="First Name is required")
        
        if not data["roll_number"]:
            raise EmptyError(status_code=400, error_code="STUDENT001", error_message="Roll Number required")
        if existing:
            student_code_existing = Student.query.filter(Student.roll_number == data["roll_number"]).first()
            if student_code_existing:
                raise UniqueError(type="roll_number", status_code=400)
            existing.first_name = data["first_name"]
            existing.roll_number = data["roll_number"]
            existing.last_name = data["last_name"]
            db.session.commit()
            return existing, 200
        elif not existing:
            raise NotFoundError(type="Student",status_code=404)
        else:
            raise InternalServerError(status_code=500)

    
    def delete(self, student_id):
        existing = Student.query.filter(Student.student_id == student_id).first()
        if existing:
            db.session.delete(existing)
            db.session.commit()
            return "Successfully Deleted", 200
        elif not existing:
            raise NotFoundError(type="Student",status_code=404)
        else:
            raise InternalServerError(status_code=500)


api.add_resource(CourseApi, "/api/course/<int:course_id>", "/api/course")
api.add_resource(StudentApi, "/api/student/<int:student_id>", "/api/student")


if __name__ == "__main__":
    app.run(debug=True)