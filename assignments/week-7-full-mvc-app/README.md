# Week 7 — Full MVC Flask Application (Students & Courses)

## 🎯 Objective

Build a **complete, production-style Flask MVC web application** with a full UI for managing Students, Courses, and their Enrollments. This is the most comprehensive assignment in the series, combining everything learned in previous weeks into a polished, navigable web app.

---

## 📁 Files

| File | Description |
|------|-------------|
| `app.py` | Main Flask app — all models, routes (controllers), and app config |
| `week7_database.sqlite3` | SQLite database (auto-created) |
| `templates/index.html` | Home — lists all students with action links |
| `templates/add_student.html` | Form to add a new student |
| `templates/update_student.html` | Form to edit a student's name and enrolled course |
| `templates/student_info.html` | Detailed view of a student and their courses |
| `templates/courses.html` | Lists all courses with action links |
| `templates/add_course.html` | Form to add a new course |
| `templates/update_course.html` | Form to update course details |
| `templates/course_info.html` | Detailed view of a course and enrolled students |
| `templates/existing.html` | Reusable error page for duplicate entry conflicts |

---

## 📖 Concepts Covered

- **MVC architecture** — clear separation of models, routes (controllers), and templates (views)
- Many-to-Many relationship between `Student` and `Course` via `Enrollments` table
- Full CRUD for **both** Students and Courses
- Enrollment management — adding/changing a student's enrolled course
- Reusable error template with dynamic messages
- Clean URL routing with Flask's `url_for()` (in templates)

---

## 🗄️ Database Schema

```
Student            Course              Enrollments
──────────         ──────────          ─────────────────
student_id    PK   course_id      PK   enrollment_id  PK
roll_number        course_code         estudent_id    FK → Student
first_name         course_name         ecourse_id     FK → Course
last_name          course_description
```

---

## ▶️ How to Run

```bash
cd "Assignments/Week 7"
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

The database is auto-created on first run.

---

## 🔄 Application Routes

### Student Routes

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Home — list all students |
| `GET/POST` | `/student/create` | Add a new student |
| `GET/POST` | `/student/<id>/update` | Edit a student |
| `GET` | `/student/<id>/delete` | Delete a student |
| `GET` | `/student/<id>` | View student details |

### Course Routes

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/courses` | List all courses |
| `GET/POST` | `/course/create` | Add a new course |
| `GET/POST` | `/course/<id>/update` | Edit a course |
| `GET` | `/course/<id>/delete` | Delete a course |
| `GET` | `/course/<id>` | View course details and enrolled students |