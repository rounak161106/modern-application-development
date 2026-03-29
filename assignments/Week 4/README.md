# Week 4 — Flask Web Application with Forms & Charts

## 🎯 Objective

Build a **Flask web application** that accepts user input via an HTML form, queries student/course data from a CSV file, and renders results — including a dynamically generated **histogram chart** for course queries.

---

## 📁 Files

| File | Description |
|------|-------------|
| `app.py` | Flask application with routing and data processing logic |
| `data.csv` | Dataset containing student IDs, course IDs, and marks |
| `static/graph.png` | Saved histogram chart (generated at runtime) |
| `templates/index.html` | Home page — form to select Student ID or Course ID |
| `templates/student.html` | Displays all courses and marks for a student |
| `templates/courses.html` | Displays average/max marks + histogram for a course |
| `templates/error.html` | Shown when invalid ID is submitted |

---

## 📖 Concepts Covered

- Flask routing (`@app.route`) with `GET` and `POST` methods
- HTML form handling with `request.form`
- Serving static files (`static/` folder)
- Jinja2 template rendering with `render_template()`
- Dynamic chart generation and saving with **Matplotlib**
- Basic data aggregation (sum, max, average) from CSV

---

## ▶️ How to Run

```bash
cd "Assignments/Week 4"
python app.py
```

Open your browser and go to: [http://localhost:5000](http://localhost:5000)

- Select **Student ID** and enter a valid ID (e.g., `1001`) to see their marks.
- Select **Course ID** and enter a valid course (e.g., `2001`) to see the course stats and histogram.

---

## 🔄 Application Flow

```
GET /  →  index.html (form)
         │
POST / ──┼── Student ID  →  student.html  (marks table)
         └── Course ID   →  courses.html  (avg, max, histogram)
                                            (invalid input → error.html)
```

---

## ⚠️ Notes

- `static/graph.png` is overwritten on every course query.
- The app reads `data.csv` at startup; changes to the CSV require a server restart.