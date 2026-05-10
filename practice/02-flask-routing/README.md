# 02 — Flask Routing & Form Handling

> **Topic**: First Flask app — understanding routes, templates, and form handling

## What This Demonstrates

Two Flask experiments:
1. **`flask_demo.py`** — A form-handling app (GET shows form → POST processes input)
2. **`main.py`** — Playground for experimenting with Flask's URL routing rules

## Files

| File | Purpose |
|------|---------|
| `flask_demo.py` | Flask app with HTML form handling (GET/POST) |
| `main.py` | Routing experiments (double slashes, trailing slashes, nested paths) |
| `templates/index.html` | HTML form template |
| `templates/display_details.html` | Template to display submitted form data |

## Concepts Covered

- `Flask(__name__)` app creation
- `@app.route()` decorator with `methods=["GET", "POST"]`
- `request.form["key"]` for accessing form data
- `render_template()` for Jinja2 HTML rendering
- Flask's URL routing engine and pattern matching

## How to Run

```bash
python flask_demo.py
# Open: http://localhost:5000
```
