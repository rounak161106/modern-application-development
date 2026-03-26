#<=============================Required imports==============================================>
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, marshal_with, fields

#<====================Configuration and setup================================================>
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api_database.sqlite3"
app.app_context().push()
db = SQLAlchemy(app)
api = Api(app)

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
output_fields = {
    "course_id": fields.Integer,
    "course_name": fields.String,
    "course_code": fields.String,
    "course_description": fields.String
}

class CourseApi(Resource):
    @marshal_with(output_fields)
    def get(self, course_id):
        course_obj = Course.query.get(course_id)
        return course_obj
        

    def push(self):
        pass

    def put(self, course_id):
        pass    
    
    def delete(self, course_id):
        pass


api.add_resource(CourseApi, "/api/course/<int:course_id>")
if __name__ == "__main__":
    app.run(debug=True)