# Week 3 — Jinja2 Templating & CLI Data Renderer

## 🎯 Objective

Build a **command-line Python application** that reads student marks from a CSV file and dynamically generates an HTML report using **Jinja2 templates**. For course queries, a histogram of marks distribution is also generated using **Matplotlib**.

---

## 📁 Files

| File | Description |
|------|-------------|
| `app.py` | Main application — parses CLI args, reads CSV, renders Jinja2 template |
| `data.csv` | Sample data with Student IDs, Course IDs, and Marks |
| `output.html` | Generated HTML file (created on run, gitignored) |
| `graph.png` | Generated histogram image (created on run, for `-c` mode) |

---

## 📖 Concepts Covered

- Command-line argument parsing with `sys.argv`
- CSV file reading and parsing
- **Jinja2 templating** — conditionals, loops, namespace variables, filters
- Data aggregation (total marks per student, average/max per course)
- Chart generation with **Matplotlib** (`plt.hist`, `plt.savefig`)
- Writing dynamic HTML to a file from Python

---

## ▶️ How to Run

```bash
cd "Assignments/Week 3"
```

**Query by Student ID:**
```bash
python app.py -s 1001
```
Generates `output.html` with a table of all courses and marks for student `1001`, along with total marks.

**Query by Course ID:**
```bash
python app.py -c 2001
```
Generates `output.html` with average and maximum marks for course `2001`, and saves a histogram as `graph.png`.

---

## 📊 Data Format (`data.csv`)

```
Student id, Course id, Marks
1001, 2001, 56
1002, 2001, 67
...
```

---

## ⚠️ Notes

- `output.html` and `graph.png` are generated files and are excluded from version control via `.gitignore`.
- The Jinja2 template is embedded directly in `app.py` as a multi-line string.