# Week 6 — RESTful API with Flask-RESTful

## 🎯 Objective

Design and implement a **RESTful API** for managing Students, Courses, and Enrollments using **Flask-RESTful**. This assignment covers proper HTTP methods, resource-based URL design, structured error handling, and JSON response formatting.

---

## 📁 Files

| File | Description |
|------|-------------|
| `app.py` | Full API implementation with models, resources, and error classes |
| `api_database.sqlite3` | SQLite database (auto-created by SQLAlchemy) |

---

## 📖 Concepts Covered

- **Flask-RESTful** — `Resource` classes, `Api` registration
- `@marshal_with` for consistent JSON output formatting
- Custom **HTTP Exception classes** for structured error responses:
  - `NotFoundError` (404)
  - `ExistingError` / `UniqueError` (409 / 400)
  - `EmptyError` (400) with structured `error_code` + `error_message`
  - `InternalServerError` (500)
- Full REST verbs: `GET`, `POST`, `PUT`, `DELETE`
- **Enrollment** sub-resource on the Student endpoint

---

## 🗄️ Database Schema

```
Course            Student           Enrollment
──────────        ──────────        ─────────────
course_id    PK   student_id   PK   enrollment_id  PK
course_name       roll_number       student_id     FK → Student
course_code       first_name        course_id      FK → Course
course_description last_name
```

---

## 🔗 API Endpoints

### Course API

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/course/<course_id>` | Get a course by ID |
| `POST` | `/api/course` | Create a new course |
| `PUT` | `/api/course/<course_id>` | Update an existing course |
| `DELETE` | `/api/course/<course_id>` | Delete a course |

### Student API

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/student/<student_id>` | Get a student by ID |
| `POST` | `/api/student` | Create a new student |
| `PUT` | `/api/student/<student_id>` | Update a student |
| `DELETE` | `/api/student/<student_id>` | Delete a student |

### Enrollment API

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/student/<student_id>/course` | Get all enrollments for a student |
| `POST` | `/api/student/<student_id>/course` | Enroll a student in a course |
| `DELETE` | `/api/student/<student_id>/course/<course_id>` | Remove a student from a course |

---

## ▶️ How to Run

```bash
cd "Assignments/Week 6"
python app.py
```

The server starts at [http://localhost:5000](http://localhost:5000).  
Use **Postman**, **Thunder Client**, or `curl` to test the API.

### Example `curl` commands

```bash
# Create a new course
curl -X POST http://localhost:5000/api/course \
  -H "Content-Type: application/json" \
  -d '{"course_name": "Flask Basics", "course_code": "MAD001"}'

# Get a student
curl http://localhost:5000/api/student/1

# Enroll student 1 in course 2
curl -X POST http://localhost:5000/api/student/1/course \
  -H "Content-Type: application/json" \
  -d '{"course_id": 2}'
```

---

## ⚠️ Error Response Format

Validation errors return structured JSON:
```json
{
  "error_code": "COURSE001",
  "error_message": "Course Name is required"
}
```