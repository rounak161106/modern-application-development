# 10 — Flask-Login: User Authentication

> **Topic**: Implementing user authentication with Flask-Login

## What This Demonstrates

A complete authentication system using the `flask-login` library, including:
- User login with credential validation
- Protected dashboard route
- User logout with session cleanup

## Files

| File | Purpose |
|------|---------|
| `app.py` | Flask app with Flask-Login authentication |
| `testdb.sqlite3` | Database with sample user accounts |
| `templates/login_form.html` | Login page with username/password form |
| `templates/dashboard.html` | Protected dashboard (only visible when logged in) |

## Authentication Flow

```
/login (GET)  → Show login form
/login (POST) → Validate credentials → login_user() → Redirect to /dashboard
/dashboard    → @login_required → Show user info via current_user
/logout       → logout_user() → Redirect to /login
```

## Concepts Covered

- `LoginManager` setup and `@login_manager.user_loader`
- `UserMixin` — provides default Flask-Login method implementations
- `login_user()` / `logout_user()` for session management
- `@login_required` decorator to protect routes
- `current_user` proxy for accessing the logged-in user
- `SECRET_KEY` requirement for session security

## How to Run

```bash
python app.py
# Open: http://localhost:5000/login
```
