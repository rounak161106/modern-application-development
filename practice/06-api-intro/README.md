# 06 — API Introduction

> **Topic**: Building REST APIs — from in-memory data to database-backed endpoints

## What This Demonstrates

Two files showing the progression of API development:

1. **`intro.py`** — API with in-memory data (not persistent)
2. **`api_with_db.py`** — API backed by an SQLAlchemy database (persistent)

## Files

| File | Purpose |
|------|---------|
| `intro.py` | First API — GET/POST with Python list data (resets on restart) |
| `api_with_db.py` | API backed by SQLite database (data persists) |
| `instance/apidb.sqlite3` | Database for the db-backed API |

## Concepts Covered

- Returning dictionaries from Flask → auto-converted to JSON
- `request.json` to parse incoming JSON data
- HTTP status codes (200, 201, 404) as second return values
- Dynamic URL parameters (`<name>`)
- The difference between in-memory and database-backed APIs
- Querying with `filter()` and `first()`

## How to Run

```bash
# In-memory API (data resets on restart)
python intro.py

# Database-backed API (data persists)
python api_with_db.py
```

> **Tip**: Use Postman, Thunder Client, or `curl` to test POST endpoints
> (browsers can only send GET requests to APIs)
