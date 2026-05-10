"""
app.py — Week 6 Assignment: RESTful API with Flask-RESTful
===========================================================
Course: Modern Application Development I (MAD-1), IIT Madras BS Program

This application implements a complete RESTful API for managing Students,
Courses, and Enrollments. It was the first time I built an API (no HTML
templates — pure JSON responses) using the Flask-RESTful extension.

The API follows REST conventions:
    - GET    → Retrieve a resource
    - POST   → Create a new resource
    - PUT    → Update an existing resource
    - DELETE → Remove a resource

Each resource returns structured JSON responses with appropriate
HTTP status codes and error handling.

Usage:
    python app.py
    Then use Postman, Thunder Client, or curl to test the endpoints.

API Endpoints:
    Course:     /api/course/<id>     (GET, PUT, DELETE)
                /api/course          (POST)
    Student:    /api/student/<id>    (GET, PUT, DELETE)
                /api/student         (POST)
    Enrollment: /api/student/<id>/course          (GET, POST)
                /api/student/<id>/course/<cid>    (DELETE)

Key concepts learned:
    - Flask-RESTful Resource classes and Api registration
    - @marshal_with decorator for consistent JSON output formatting
    - Custom HTTP exception classes for structured error responses
    - Proper HTTP status codes (200, 201, 400, 404, 409, 500)
    - Validation and error handling with descriptive error codes
    - Enrollment as a sub-resource on the Student endpoint
"""

# ──────────────────────────────────────────────────────────
# Imports
# ──────────────────────────────────────────────────────────
from flask import Flask, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, marshal_with, fields
import json
from werkzeug.exceptions import HTTPException    # Base class for custom HTTP errors

# ──────────────────────────────────────────────────────────
# Custom Error Classes
# ──────────────────────────────────────────────────────────
# These custom exception classes provide structured error responses
# instead of Flask's default HTML error pages. Each one sets the
# HTTP status code and a descriptive error message.

class NotFoundError(HTTPException):
    """Raised when a requested resource (Student, Course) doesn't exist. Returns 404."""
    def __init__(self, status_code, type):
        super().__init__()
        self.code = status_code
        self.data = f'{type} not found'

class InternalServerError(HTTPException):
    """Raised for unexpected server-side errors. Returns 500."""
    def __init__(self, status_code):
        super().__init__()
        self.code = status_code
        self.data = 'Internal Server Error'

class ExistingError(HTTPException):
    """Raised when trying to create a resource that already exists. Returns 409."""
    def __init__(self, status_code, type):
        super().__init__()
        self.code = status_code
        self.data = f'{type} already exist'

class EmptyError(HTTPException):
    """
    Raised when a required field is missing in the request body.
    Returns a structured JSON error with error_code and error_message.
    Example: {"error_code": "COURSE001", "error_message": "Course Name is required"}
    """
    def __init__(self, status_code, error_code, error_message):
        super().__init__()
        message = {"error_code" : error_code, "error_message" : error_message}
        self.code = status_code
        self.data = message

class UniqueError(HTTPException):
    """Raised when a unique constraint would be violated (e.g., duplicate course code)."""
    def __init__(self, status_code, type):
        super().__init__()
        self.code = status_code
        self.data = f'{type} already exist'
        

# ──────────────────────────────────────────────────────────
# Flask App Configuration
# ──────────────────────────────────────────────────────────
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///api_database.sqlite3"
app.app_context().push()
db = SQLAlchemy(app)
api = Api(app)

# ──────────────────────────────────────────────────────────
# Database Models
# ──────────────────────────────────────────────────────────
# These are the same Student-Course-Enrollment models from Week 5,
# but this time they're used purely for API access (no HTML templates).

class Course(db.Model):
    """Course model — represents a course in the system."""
    course_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    course_name = db.Column(db.String, nullable = False)
    course_code = db.Column(db.String, nullable = False, unique = True)
    course_description = db.Column(db.String)
    students = db.relationship("Student", secondary="enrollment", backref="courses")

class Student(db.Model):
    """Student model — represents a student in the system."""
    student_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    roll_number = db.Column(db.String, nullable = False, unique = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)


class Enrollment(db.Model):
    """Junction table linking students to courses (Many-to-Many)."""
    enrollment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    student_id = db.Column(db.Integer, db.ForeignKey(Student.student_id),nullable = False)
    course_id = db.Column(db.Integer, db.ForeignKey(Course.course_id),nullable = False)

# ──────────────────────────────────────────────────────────
# Course API Resource
# ──────────────────────────────────────────────────────────
# Output fields define the JSON structure returned by @marshal_with.
# This ensures consistent response formatting regardless of the
# model's internal attributes.
course_output_fields = {
    "course_id": fields.Integer,
    "course_name": fields.String,
    "course_code": fields.String,
    "course_description": fields.String
}

class CourseApi(Resource):
    """
    RESTful resource for Course CRUD operations.
    
    GET    /api/course/<id>  → Retrieve a course by ID
    POST   /api/course       → Create a new course
    PUT    /api/course/<id>  → Update an existing course
    DELETE /api/course/<id>  → Delete a course
    """
    @marshal_with(course_output_fields)
    def get(self, course_id):
        """Retrieve a single course by its ID."""
        course_obj = Course.query.get(course_id)
        if course_obj:
            return course_obj, 200
        elif not course_obj :
            raise NotFoundError(type="Course",status_code=404)
        else:
            raise InternalServerError(status_code=500)
        
    @marshal_with(course_output_fields)
    def post(self):
        """
        Create a new course. Expects JSON body with:
        - course_code (required, must be unique)
        - course_name (required)
        - course_description (optional)
        """
        data = request.json or {}
        course_code_list = Course.query.all()
        course_codes = [i.course_code for i in course_code_list]
        
        # Validate required fields
        if not data.get("course_code"):
            raise EmptyError(status_code=400, error_code="COURSE002", error_message="Course Code is required")
        
        if not data.get("course_name"):
            raise EmptyError(status_code=400, error_code="COURSE001", error_message="Course Name is required")
        
        # Check for duplicate course codes
        if data.get("course_code") in course_codes:
            raise ExistingError(status_code=409, type="course_code")
        
        # Create and save the new course
        if data.get("course_code") not in course_codes:
            new_course = Course(course_code = data.get("course_code"), course_name = data.get("course_name"), course_description = data.get("course_description"))
            db.session.add(new_course)
            db.session.commit()
            return new_course, 201
        else:
            raise InternalServerError(status_code=500)

    @marshal_with(course_output_fields)
    def put(self, course_id):
        """Update an existing course's details."""
        data = request.json or {}
        existing = Course.query.filter(Course.course_id == course_id).first()
        
        # Validate required fields
        if not data.get("course_code"):
            raise EmptyError(status_code=400, error_code="COURSE002", error_message="Course Code is required")
        
        if not data.get("course_name"):
            raise EmptyError(status_code=400, error_code="COURSE001", error_message="Course Name is required")
        
        if existing:
            # Check that the new course_code doesn't conflict with another course
            course_code_existing = Course.query.filter(Course.course_code == data.get("course_code")).first()
            if course_code_existing and course_code_existing.course_id != course_id:
                raise UniqueError(type="course_id", status_code=400)
            existing.course_name = data.get("course_name")
            existing.course_code = data.get("course_code")
            existing.course_description = data.get("course_description")
            db.session.commit()
            return existing, 200
        elif not existing:
            raise NotFoundError(type="Course",status_code=404)
        else:
            raise InternalServerError(status_code=500)

    
    def delete(self, course_id):
        """Delete a course by its ID."""
        existing = Course.query.filter(Course.course_id == course_id).first()
        if existing:
            db.session.delete(existing)
            db.session.commit()
            return "Successfully Deleted", 200
        elif not existing:
            raise NotFoundError(type="Course",status_code=404)
        else:
            raise InternalServerError(status_code=500)
        
# ──────────────────────────────────────────────────────────
# Student API Resource
# ──────────────────────────────────────────────────────────
student_output_fields = {
    "student_id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "roll_number": fields.String
}

class StudentApi(Resource):
    """
    RESTful resource for Student CRUD operations.
    
    GET    /api/student/<id>  → Retrieve a student by ID
    POST   /api/student       → Create a new student
    PUT    /api/student/<id>  → Update an existing student
    DELETE /api/student/<id>  → Delete a student
    """
    @marshal_with(student_output_fields)
    def get(self, student_id):
        """Retrieve a single student by their ID."""
        student_obj = Student.query.get(student_id)
        if student_obj:
            return student_obj, 200
        elif not student_obj :
            raise NotFoundError(type = "Student", status_code=404)
        else:
            raise InternalServerError(status_code=500)
        
    @marshal_with(student_output_fields)
    def post(self):
        """
        Create a new student. Expects JSON body with:
        - roll_number (required, must be unique)
        - first_name (required)
        - last_name (optional)
        """
        data = request.json or {}
        student_code_list = Student.query.all()
        student_codes = [i.roll_number for i in student_code_list]
        
        # Validate required fields
        if not data.get("roll_number"):
            raise EmptyError(status_code=400, error_code="STUDENT001", error_message="Roll Number required")
        
        if not data.get("first_name"):
            raise EmptyError(status_code=400, error_code="STUDENT002", error_message="First Name is required")
        
        # Check for duplicate roll numbers
        if data.get("roll_number") in student_codes:
            raise ExistingError(status_code=409, type="Student")
        
        # Create and save the new student
        if data.get("roll_number") not in student_codes:
            new_student = Student(roll_number = data.get("roll_number"), first_name = data.get("first_name"), last_name = data.get("last_name"))
            db.session.add(new_student)
            db.session.commit()
            return new_student, 201
        else:
            raise InternalServerError(status_code=500)

    @marshal_with(student_output_fields)
    def put(self, student_id):
        """Update an existing student's details."""
        data = request.json or {}
        existing = Student.query.filter(Student.student_id == student_id).first()
        
        # Validate required fields
        if not data.get("first_name"):
            raise EmptyError(status_code=400, error_code="STUDENT002", error_message="First Name is required")
        
        if not data.get("roll_number"):
            raise EmptyError(status_code=400, error_code="STUDENT001", error_message="Roll Number required")
        
        if existing:
            # Check that the new roll_number doesn't conflict with another student
            student_code_existing = Student.query.filter(Student.roll_number == data.get("roll_number")).first()
            if student_code_existing and student_code_existing.student_id != student_id:
                raise UniqueError(type="roll_number", status_code=400)
            existing.first_name = data.get("first_name")
            existing.roll_number = data.get("roll_number")
            existing.last_name = data.get("last_name")
            db.session.commit()
            return existing, 200
        elif not existing:
            raise NotFoundError(type="Student",status_code=404)
        else:
            raise InternalServerError(status_code=500)

    
    def delete(self, student_id):
        """Delete a student by their ID."""
        existing = Student.query.filter(Student.student_id == student_id).first()
        if existing:
            db.session.delete(existing)
            db.session.commit()
            return "Successfully Deleted", 200
        elif not existing:
            raise NotFoundError(type="Student",status_code=404)
        else:
            raise InternalServerError(status_code=500)


# ──────────────────────────────────────────────────────────
# Enrollment API Resource
# ──────────────────────────────────────────────────────────
class EnrollmentApi(Resource):
    """
    RESTful resource for managing student-course enrollments.
    Enrollments are a sub-resource of Student, so the URL pattern is:
    /api/student/<student_id>/course
    
    GET    → List all courses a student is enrolled in
    POST   → Enroll a student in a course
    DELETE → Remove a student from a course
    """
    def get(self, student_id):
        """Get all enrollments for a specific student."""
        existing = Enrollment.query.filter_by(student_id = student_id).all()
        studentexist = Student.query.filter_by(student_id = student_id).all()
        if not studentexist:
            raise EmptyError(status_code=400, error_code="ENROLLMENT002", error_message="Student does not exist.")
        if not existing:
            return "Student is not enrolled in any course", 404
        if existing:
            # Manually build the JSON response (no @marshal_with for custom structure)
            enrolls = [{"enrollment_id": i.enrollment_id,"student_id": i.student_id,"course_id": i.course_id} for i in existing]
            return enrolls, 200
        else:
            raise InternalServerError(status_code=500)

    def post(self, student_id):
        """Enroll a student in a course. Expects JSON body with course_id."""
        studentexist = Student.query.filter_by(student_id = student_id).all()
        if not studentexist:
            return "Student not found", 404
        data = request.json or {}
        course = Course.query.filter_by(course_id = data.get("course_id")).first() if data.get("course_id") else None
        if not course:
            raise EmptyError(status_code=400, error_code="ENROLLMENT001", error_message="Course does not exist")
        if course:
            new = Enrollment(student_id = student_id, course_id = data.get("course_id"))
            db.session.add(new)
            db.session.commit()
            return [{"enrollment_id": new.enrollment_id,"student_id": new.student_id,"course_id": new.course_id}], 201
        else:
            raise InternalServerError(status_code=500)

    def delete(self, student_id, course_id):
        """Remove a student from a specific course."""
        stu_exist = Student.query.filter_by(student_id = student_id).first()
        course_exist = Course.query.filter_by(course_id = course_id).first()
        if not stu_exist:
            raise EmptyError(status_code=400, error_code="ENROLLMENT002", error_message="Student does not exist.")
        if not course_exist:
            raise EmptyError(status_code=400, error_code="ENROLLMENT001", error_message="Course does not exist")
        enrolls = Enrollment.query.filter(Enrollment.student_id == student_id, Enrollment.course_id == course_id).first()
        if not enrolls:
            return "Enrollment for the student not found", 404
        elif enrolls:
            db.session.delete(enrolls)
            db.session.commit()
            return "Successfully deleted", 200
        else:
            raise InternalServerError(status_code=500)
            
# ──────────────────────────────────────────────────────────
# Register API Endpoints
# ──────────────────────────────────────────────────────────
# Each Resource class is mapped to one or more URL patterns.
# Flask-RESTful automatically routes HTTP methods (GET, POST, etc.)
# to the corresponding methods in the Resource class.
api.add_resource(CourseApi, "/api/course/<int:course_id>", "/api/course")
api.add_resource(StudentApi, "/api/student/<int:student_id>", "/api/student")
api.add_resource(EnrollmentApi, '/api/student/<int:student_id>/course', '/api/student/<int:student_id>/course/<int:course_id>')

# ──────────────────────────────────────────────────────────
# Run the App
# ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True)