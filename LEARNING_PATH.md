# 🗺️ Learning Path — Where to Start

> This guide maps out the complete learning journey of this repository.
> If you're new here, follow this path from top to bottom.

---

## Phase 1: Web Fundamentals (Week 2)

**Start here** — the very beginning of web development.

📂 [`assignments/week-2-html-fundamentals/`](./assignments/week-2-html-fundamentals/)

What you'll learn:
- HTML5 document structure (`<!DOCTYPE>`, `<html>`, `<head>`, `<body>`)
- Building a multi-page static website
- Navigation between pages using `<a>` tags
- HTML tables for displaying structured data
- Images, links, and the `<address>` element

---

## Phase 2: Templating with Jinja2 (Week 3)

The transition from static HTML to **dynamic content generation**.

📂 [`assignments/week-3-jinja2-templating/`](./assignments/week-3-jinja2-templating/)
📂 [`practice/01-jinja2-standalone/`](./practice/01-jinja2-standalone/) *(optional — extra practice)*

What you'll learn:
- Jinja2 template syntax (`{% for %}`, `{{ variable }}`, `{% if %}`)
- `namespace()` for mutable variables inside loops
- Generating HTML files from Python data
- Reading CSV files with Python's `csv` module
- Chart generation with Matplotlib

---

## Phase 3: Flask Web Framework (Week 4)

Moving from the command line to **browser-based web applications**.

📂 [`assignments/week-4-flask-basics/`](./assignments/week-4-flask-basics/)
📂 [`practice/02-flask-routing/`](./practice/02-flask-routing/) *(optional — routing experiments)*

What you'll learn:
- Flask app creation and routing (`@app.route()`)
- Handling GET and POST requests
- HTML form processing with `request.form`
- Rendering templates with `render_template()`
- Serving static files (images, CSS, JS)

---

## Phase 4: Database ORM (Weeks 5-7)

The **biggest learning leap** — from flat files to relational databases.

### Step 1: Understand raw SQLAlchemy
📂 [`practice/03-sqlalchemy-without-flask/`](./practice/03-sqlalchemy-without-flask/)

### Step 2: Integrate with Flask
📂 [`practice/04-flask-sqlalchemy/`](./practice/04-flask-sqlalchemy/)
📂 [`practice/05-flask-sqlalchemy-project/`](./practice/05-flask-sqlalchemy-project/)

### Step 3: Tutorial — One-to-Many vs Many-to-Many
📂 [`tutorials/flask-sqlalchemy/`](./tutorials/flask-sqlalchemy/)

### Step 4: Graded assignment — full CRUD
📂 [`assignments/week-5-flask-sqlalchemy/`](./assignments/week-5-flask-sqlalchemy/)

What you'll learn:
- SQLAlchemy ORM (models, sessions, transactions)
- One-to-Many and Many-to-Many relationships
- Junction/association tables
- Full CRUD operations (Create, Read, Update, Delete)
- PRG pattern (Post-Redirect-Get)

---

## Phase 5: REST APIs (Week 6)

Building **backend APIs** — no HTML, pure JSON responses.

### Step 1: Start with simple APIs
📂 [`practice/06-api-intro/`](./practice/06-api-intro/)

### Step 2: Tutorial — Flask-RESTful
📂 [`tutorials/flask-restful-instructor/`](./tutorials/flask-restful-instructor/)
📂 [`tutorials/flask-restful-practice/`](./tutorials/flask-restful-practice/)

### Step 3: Graded assignment — complete REST API
📂 [`assignments/week-6-rest-api/`](./assignments/week-6-rest-api/)

What you'll learn:
- REST conventions (GET, POST, PUT, DELETE)
- Flask-RESTful `Resource` classes
- `@marshal_with` for consistent JSON output
- Custom HTTP exception classes
- Request validation and error codes

---

## Phase 6: Full MVC Application (Week 7)

**Everything comes together** — the capstone assignment.

📂 [`assignments/week-7-full-mvc-app/`](./assignments/week-7-full-mvc-app/)

What you'll learn:
- MVC architecture (Models, Views, Controllers)
- Complete web application with Student + Course management
- Enrollment management (Many-to-Many CRUD)
- Reusable error templates

---

## Bonus: Beyond the Syllabus 🚀

These topics were explored **out of personal curiosity** — not part of the graded coursework.

| Topic | Folder | Why I Explored It |
|-------|--------|-------------------|
| JavaScript & DOM | [`practice/07-javascript-basics/`](./practice/07-javascript-basics/) | Wanted to understand the frontend side |
| Python Logging | [`practice/08-logging/`](./practice/08-logging/) | Better debugging than `print()` |
| PostgreSQL (psycopg2) | [`practice/09-psycopg2-postgresql/`](./practice/09-psycopg2-postgresql/) | Real-world databases beyond SQLite |
| Sessions & Cookies | [`tutorials/sessions-and-cookies/`](./tutorials/sessions-and-cookies/) | How auth works at a lower level |
| Flask-Login Auth | [`practice/10-flask-login/`](./practice/10-flask-login/) | User authentication system |
| Testing (Pytest) | [`practice/11-testing-pytest/`](./practice/11-testing-pytest/) | Writing automated tests |

---

## 📊 Skills Progression

```
Week 2:  HTML ████░░░░░░░░░░░░  Static pages
Week 3:  +Jinja2 ██████░░░░░░░░  Dynamic content generation
Week 4:  +Flask ████████░░░░░░  Web server + forms
Week 5:  +SQLAlchemy ██████████░░  Database integration + CRUD
Week 6:  +REST API ████████████░  Backend API development
Week 7:  +MVC █████████████  Full-stack web application
Bonus:   +Auth +Testing ██████████████  Production-ready skills
```

---

> 💡 **Tip**: Each folder has its own `README.md` with more detailed explanations,
> file descriptions, and "How to Run" instructions.
