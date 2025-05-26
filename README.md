# Articles Challenge

This project models the relationship between Authors, Articles, and Magazines using Python and raw SQL queries. It uses SQLite as the database backend and includes classes for each entity with methods to save, query, and manage data.

## Features

- Models Author, Article, and Magazine entities with relationships.
- Implements many-to-many relationships between Authors and Magazines via Articles.
- Supports adding, querying, and listing related records.
- Uses raw SQL queries inside Python classes for data persistence.
- Includes unit tests using pytest for all core functionalities.
- Supports database transactions and error handling.
- Organized project structure with separate modules for models, database connection, schema, and tests.

## Setup Instructions

1. Create a virtual environment and activate it.
2. Install dependencies with `pip install -r requirements.txt` (if you have one).
3. Run `python scripts/setup_db.py` to create and seed the database.
4. Use `pytest` to run tests and verify implementation.

## Technologies Used

- Python 3.8+
- SQLite
- pytest

---

Feel free to tweak that to add any personal notes or instructions you want!

---

### 2. Add a Python `.gitignore`

Next, create a `.gitignore` file to avoid pushing unnecessary files:

```bash
cat <<EOF > .gitignore
__pycache__/
*.pyc
env/
venv/
*.db
.pytest_cache/
.idea/
.vscode/
*.log
EOF

