# Week 5 — Flask + SQLAlchemy CRUD Application

## 🎯 Objective

Build a **full CRUD web application** using Flask and Flask-SQLAlchemy to manage students and their course enrollments, backed by an SQLite database. This assignment introduces ORM-based database interactions replacing raw CSV/SQL.

---

## 📁 Files

| File | Description |
|------|-------------|
| `app.py` | Flask app with all routes and SQLAlchemy models |
| `instance/database.sqlite3` | SQLite database (auto-created by SQLAlchemy) |
| `templates/home.html` | Lists all students |
| `templates/create.html` | Form to add a new student with course selection |
| `templates/update.html` | Form to edit an existing student's data |
| `templates/show_details.html` | Detailed view of a single student and their courses |
| `templates/exists.html` | Shown when a duplicate roll number is submitted |

---

## 📖 Concepts Covered

- **Flask-SQLAlchemy** ORM setup and configuration
- Defining database **models** (`Student`, `Course`, `Enrollments`)
- **Many-to-Many** relationship using a junction table (`Enrollments`)
- Full **CRUD** operations:
  - **Create** — add new students with selected courses
  - **Read** — list all students, view individual details
  - **Update** — modify student info and course enrollments
  - **Delete** — remove a student record
- `redirect()` after POST to follow the PRG (Post-Redirect-Get) pattern
- Querying with `Model.query.all()`, `.get()`, `.filter_by()`

---

## 🗄️ Database Schema

```
Student          Course           Enrollments
──────────       ──────────       ─────────────
student_id  PK   course_id   PK   enrollment_id  PK
roll_number      course_code      estudent_id    FK → Student
first_name       course_name      ecourse_id     FK → Course
last_name        course_description
```

---

## ▶️ How to Run

```bash
cd "Assignments/Week 5"
python app.py
```

Open your browser at: [http://localhost:5000](http://localhost:5000)

The database will be automatically created in the `instance/` folder on first run.

---

## 🔄 Application Routes

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Home — list all students |
| `GET/POST` | `/student/create` | Add a new student |
| `GET/POST` | `/student/<id>/update` | Update student details |
| `GET` | `/student/<id>/delete` | Delete a student |
| `GET` | `/student/<id>` | View student details |