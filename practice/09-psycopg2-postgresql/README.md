# 09 — Psycopg2: PostgreSQL from Python

> **Topic**: Connecting to PostgreSQL directly — beyond the course syllabus 🚀

## What This Demonstrates

This was my **self-driven exploration** into working with a production-grade
database (PostgreSQL) directly from Python, using the `psycopg2` library.
The course used SQLite, but I wanted to understand how real-world databases work.

## Files

| File | Purpose |
|------|---------|
| `intro.py` | Basic PostgreSQL connection, query execution, and cleanup |
| `experiment.py` | Creating tables and inserting data programmatically |
| `encoding.py` | Character encoding/cipher exercise on query results |
| `jersey_no.py` | Query practice — fetching specific player data |
| `prime_jersey.py` | Finding players with prime jersey numbers (math + SQL) |

## Concepts Covered

- `psycopg2.connect()` for PostgreSQL connections
- Cursor objects for query execution
- `fetchall()` and `fetchone()` for retrieving results
- Transaction handling (commit/rollback)
- Proper resource cleanup (closing cursor and connection)
- Combining Python logic (prime number check) with SQL queries

## ⚠️ Note

Database credentials in these files are hardcoded for learning purposes.
In production, always use environment variables (`os.environ.get("DB_PASSWORD")`).

## Prerequisites

- PostgreSQL server running locally
- `psycopg2` library installed: `pip install psycopg2`
- A database named `flis` with player/team tables
