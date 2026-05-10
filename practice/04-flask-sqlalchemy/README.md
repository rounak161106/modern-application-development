# 04 — Flask-SQLAlchemy Practice

> **Topic**: Integrating SQLAlchemy with Flask for a web-based CRUD application

## What This Demonstrates

An Author-Article management system built with Flask-SQLAlchemy, featuring a Many-to-Many relationship. This was practice before the Week 5 assignment.

## Files

| File | Purpose |
|------|---------|
| `main.py` | Flask app with Author & Article models (M2M relationship) |
| `testdb.sqlite3` | SQLite database with sample data |
| `templates/index.html` | Home page listing articles |
| `templates/create.html` | Form to create new articles |
| `templates/create_author.html` | Form to create new authors |
| `templates/article_by.html` | View articles by a specific author |

## Concepts Covered

- Flask-SQLAlchemy setup (`SQLAlchemy(app)`, `app.config`)
- Many-to-Many relationship with junction table
- CRUD operations (Create, Read)
- Template-based UI with forms
- Navigating relationships in Jinja2 templates
