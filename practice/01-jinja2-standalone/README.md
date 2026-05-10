# 01 — Standalone Jinja2 Demo

> **Topic**: Using Jinja2 as a standalone templating engine (outside Flask)

## What This Demonstrates

This was one of my first Python experiments — using the **Jinja2 templating engine** directly from a Python script to generate an HTML file dynamically.

The key insight: **Jinja2 is NOT tied to Flask**. It's an independent library that Flask happens to use for rendering templates.

## Files

| File | Purpose |
|------|---------|
| `dynamic_table_generation.py` | Python script that renders student data into an HTML table |
| `index.html` | The generated output HTML file |

## Concepts Covered

- `Template()` class from Jinja2
- `{% for %}` loops for iterating over data
- `{{ variable }}` syntax for outputting values
- `Template.render()` to produce final HTML
- Writing generated content to an `.html` file

## How to Run

```bash
python dynamic_table_generation.py
# Opens: index.html (generated in the same directory)
```
