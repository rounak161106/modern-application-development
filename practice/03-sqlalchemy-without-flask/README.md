# 03 — SQLAlchemy Without Flask

> **Topic**: Learning the ORM layer independently, before using Flask-SQLAlchemy

## What This Demonstrates

Using **raw SQLAlchemy** (without Flask) to understand the ORM at a fundamental level. This was essential preparation for the Flask-SQLAlchemy assignments.

The code progresses through three learning stages (visible in the commented-out sections):
1. **Basic querying** with `select()` and `Session`
2. **Transaction handling** with `commit` and `rollback`
3. **Relationships** — using `relationship()` instead of manual junction table inserts

## Files

| File | Purpose |
|------|---------|
| `main.py` | SQLAlchemy ORM demo with Author-Article Many-to-Many |
| `testdb.sqlite3` | SQLite database with sample data |

## Concepts Covered

- `create_engine()` for database connection
- `declarative_base()` as the base class for models
- `Session` for managing database operations
- `relationship()` with `secondary` for Many-to-Many
- Transaction handling (`try/except` with `commit/rollback`)

## How to Run

```bash
python main.py
```
