# 📚 MAD-1 — Modern Application Development I

> **IIT Madras BS in Data Science and Applications**  
> Course: `Modern Application Development – I (MAD1)` | Diploma Level – Programming

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?logo=sqlite)
![Jinja2](https://img.shields.io/badge/Jinja2-Templates-green)
![License](https://img.shields.io/badge/License-Academic-lightgrey)

---

## 📌 About This Repository

This repository contains all my **weekly assignments**, **practice projects**, and **learning demos** for the **Modern Application Development – I (MAD-1)** course, part of the [IIT Madras BS in Data Science and Applications](https://study.iitm.ac.in/ds/) program.

The course focuses on building modern, full-stack web applications using Python, starting from static HTML pages, progressing through templating with Jinja2, building Flask web apps, integrating relational databases with SQLAlchemy, and finally designing RESTful APIs.

**Student:** Rounak Prasad  
**Roll Number:** 25f2003256  
**Batch:** 2026  
**Program:** BS in Data Science and Applications, IIT Madras

---

## 🗂️ Repository Structure

```
MAD-1/
│
├── Assignments/
│   ├── Week 2/          → Static HTML personal portfolio pages
│   ├── Week 3/          → CLI app using Jinja2 templates + Matplotlib
│   ├── Week 4/          → Flask web app with CSV data & chart generation
│   ├── Week 5/          → Flask + SQLAlchemy CRUD (Student & Course management)
│   ├── Week 6/          → RESTful API with Flask-RESTful
│   └── Week 7/          → Full Flask MVC app (Students, Courses, Enrollments)
│
├── Tutorials/           → Code written along with course tutorials
│   └── Flask_Sqlalchemy/
│
├── Flask_demo/          → Minimal Flask "Hello World" style demo
├── Flask_sqlalchemy/    → One-to-Many & Many-to-Many ORM practice
├── Flask_SQLAlchemy_Project/ → Many-to-Many project with Roles & Users
├── Jinja_demo/          → Standalone Jinja2 dynamic table generation
├── SQLAlchemy_demo/     → Raw SQLAlchemy (without Flask) demo
├── API/                 → Introductory REST API concepts
│
├── requirements.txt     → Python dependencies
├── .gitignore           → Ignored files (caches, DBs, etc.)
└── README.md            → You are here
```

---

## 📅 Assignment Breakdown

| Week | Topic | Key Technologies | Description |
|------|-------|-----------------|-------------|
| [Week 2](./Assignments/Week%202/README.md) | HTML Fundamentals | HTML5 | Static personal portfolio with navigation across 5 pages |
| [Week 3](./Assignments/Week%203/README.md) | Jinja2 Templating | Python, Jinja2, Matplotlib, CSV | CLI app that renders student/course data as HTML from command-line args |
| [Week 4](./Assignments/Week%204/README.md) | Flask Basics | Flask, HTML Forms, Matplotlib | Web form to query student/course marks with histogram charts |
| [Week 5](./Assignments/Week%205/README.md) | Flask + ORM | Flask, Flask-SQLAlchemy, SQLite | Full CRUD web app for managing students and course enrollments |
| [Week 6](./Assignments/Week%206/README.md) | REST API | Flask-RESTful, SQLAlchemy | RESTful API for Students, Courses, and Enrollments with proper HTTP methods and error handling |
| [Week 7](./Assignments/Week%207/README.md) | Full MVC App | Flask, SQLAlchemy, Jinja2 | Complete student–course management system with UI for all CRUD operations |

---

## 🛠️ Technologies Used

| Category | Tools / Libraries |
|----------|------------------|
| **Language** | Python 3.11 |
| **Web Framework** | Flask |
| **ORM** | Flask-SQLAlchemy, SQLAlchemy |
| **REST API** | Flask-RESTful |
| **Database** | SQLite3 |
| **Templating** | Jinja2 |
| **Data Visualization** | Matplotlib |
| **Frontend** | HTML5, CSS3 |
| **Data** | CSV (pandas-free raw parsing) |

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10 or above
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running an Assignment

Navigate to the specific week's folder and follow its `README.md`. For example, to run the Week 5 Flask app:

```bash
cd "Assignments/Week 5"
python app.py
```

Then open your browser at `http://localhost:5000`.

---

## 🎓 About the Course

The **MAD-1** course is part of the Diploma in Programming track of the IIT Madras online degree program. It covers the complete lifecycle of building a web application:

- Designing multi-page static websites with HTML/CSS
- Dynamic HTML generation using Jinja2 templating
- Building web servers with Flask (routing, forms, request handling)
- Database design and ORM-based CRUD using SQLAlchemy
- REST API design following HTTP conventions (GET, POST, PUT, DELETE)
- Error handling, validation, and response structuring

The program is unique in its online-first delivery combined with in-person proctored exams, making it accessible to learners across India and globally.

---

## 📂 Practice & Demos

Beyond the graded assignments, this repo also includes self-driven practice work:

| Folder | Description |
|--------|-------------|
| `Flask_demo/` | Minimal Flask routing and template rendering |
| `Jinja_demo/` | Standalone Jinja2 HTML generation from Python data |
| `SQLAlchemy_demo/` | Direct SQLAlchemy queries without Flask |
| `Flask_sqlalchemy/` | One-to-Many and Many-to-Many ORM relationships |
| `Flask_SQLAlchemy_Project/` | Role-based user management with Many-to-Many relationships |
| `API/` | Introductory REST API – basic routes, JSON responses, POST with `curl`/Postman |
| `Tutorials/` | Code written live during course tutorial sessions |

---

## 🚀 Future Improvements

- [ ] Add front-end styling with Bootstrap or Tailwind CSS
- [ ] Add authentication (Flask-Login / JWT)
- [ ] Write unit tests for API endpoints
- [ ] Deploy a live demo (Render / Railway / Heroku)
- [ ] Extend to MAD-2 coursework

---

## 📬 Contact

**Rounak Prasad**  
IIT Madras BS Program | 2026 Batch  
Roll No: `25f2003256`