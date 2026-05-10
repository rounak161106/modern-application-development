# 05 — Flask-SQLAlchemy Project: Role-Based User Management

> **Topic**: A structured Flask project with separated models and full CRUD

## What This Demonstrates

A more mature Flask application where database models are defined in a **separate file** (`models.py`) and imported into the main app. This is closer to how production Flask apps are organized.

## Files

| File | Purpose |
|------|---------|
| `main.py` | Flask app with role CRUD routes |
| `models.py` | Database models (User, Role, Association) in a separate module |
| `templates/index.html` | Home page listing all roles |
| `templates/create_role.html` | Form to create a new role |
| `templates/edit_role.html` | Form to edit an existing role |
| `templates/role_users.html` | View all users assigned to a role |

## Key Learning: Model Separation

```python
# models.py — define db and models here
db = SQLAlchemy()

# main.py — import and bind to app
from models import *
db.init_app(app)
```

This `db.init_app(app)` pattern allows the models to be defined independently of the Flask app instance.

## Concepts Covered

- Code organization: separating models from routes
- `db.init_app(app)` for late binding
- Full CRUD (Create, Read, Update, Delete) on the Role model
- Many-to-Many relationship navigation via backref
