# 08 — Python Logging

> **Topic**: Using `logging` module instead of `print()` for debugging

## What This Demonstrates

A simple Flask app that uses Python's `logging` module to write log messages
to a file (`debug.log`) instead of printing to the terminal.

## Files

| File | Purpose |
|------|---------|
| `loggers.py` | Flask app with logging configured |
| `Templates/index.html` | Simple home page template |

## Why Logging > Print

| Feature | `print()` | `logging` |
|---------|-----------|-----------|
| Save to file | ❌ | ✅ |
| Severity levels | ❌ | ✅ (DEBUG, INFO, WARNING, ERROR) |
| Filtering | ❌ | ✅ |
| Production use | ❌ | ✅ |

## How to Run

```bash
python loggers.py
# Check: debug.log file for recorded messages
```
