#<=============================Required imports==============================================>
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, marshal_with, fields
from flask_cors import CORS
import json
from werkzeug.exceptions import HTTPException    #to handle exceptions

class NotFoundError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('Course not found', status_code)
class InternalServerError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('Internal Server Error', status_code)
class ExistingError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('course_code already exist', status_code)
class CourseNotFound(HTTPException):
    def __init__(self, status_code):
        self.response = make_response('Course not found', status_code)
class EmptyCourseError(HTTPException):
    def __init__(self, status_code, error_code, error_message):
        message = {"error_code" : error_code, "error_message" : error_message}
        self.response = make_response(json.dumps(message), status_code)

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
            raise NotFoundError(status_code=404)
        else:
            raise InternalServerError(status_code=500)
        
    @marshal_with(course_output_fields)
    def post(self):
        data = request.json
        course_code_list = Course.query.all()
        course_codes = [i.course_code for i in course_code_list]
        if not data["course_code"]:
            raise EmptyCourseError(status_code=400, error_code="COURSE002", error_message="Course Code is required")
        
        if not data["course_name"]:
            raise EmptyCourseError(status_code=400, error_code="COURSE001", error_message="Course Name is required")
        
        if data["course_code"] in course_codes:
            raise ExistingError(status_code=409)
        
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
        if existing:
            existing.course_name = data["course_name"]
            existing.course_code = data["course_code"]
            existing.course_description = data["course_description"]
            db.session.commit()
            return course_output_fields, 
        else:
            raise CourseNotFound(status_code=404)

    
    def delete(self, course_id):
        pass


api.add_resource(CourseApi, "/api/course/<int:course_id>", "/api/course")
if __name__ == "__main__":
    app.run(debug=True)