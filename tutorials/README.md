# 📖 Tutorials — Live Course Session Code

> This folder contains code I wrote during **live tutorial sessions**
> from the MAD-1 course. These are code-along exercises done with the
> instructor, covering core Flask and SQLAlchemy concepts.

## 📁 Contents

| Folder | Topic | What We Covered |
|--------|-------|-----------------|
| [flask-sqlalchemy](./flask-sqlalchemy/) | ORM Relationships | One-to-Many (`main.py`) vs Many-to-Many (`main2.py`) models |
| [flask-restful-instructor](./flask-restful-instructor/) | RESTful API (instructor) | Flask-RESTful Resource classes, Employee API with GET/POST |
| [flask-restful-practice](./flask-restful-practice/) | RESTful API (follow-along) | Author API with error handling, `@marshal_with`, `reqparse` |
| [sessions-and-cookies](./sessions-and-cookies/) | Session Management | Flask sessions, login/dashboard/logout without Flask-Login |

## 🔑 Key Difference from Practice

These tutorials were **structured, instructor-led sessions** — different from
the hands-on practice exercises in the `practice/` folder. They follow the course
curriculum closely and served as the foundation for the graded assignments.

## 📌 Notable Learnings

- **`flask-sqlalchemy/`**: Side-by-side comparison of One-to-Many vs Many-to-Many
  using the same User-Role domain — helped clarify when to use each pattern
- **`flask-restful-instructor/`**: First exposure to separating `models.py` from
  `app.py` — a pattern I later used in my own projects
- **`sessions-and-cookies/`**: Understanding raw sessions before using Flask-Login
  made the authentication concepts much clearer
