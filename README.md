# MongoDB Exercise 4 – Online Collaborative Document Editor

This project demonstrates a simple **document-based data model** using **MongoDB** and **PyMongo** for a collaborative document editing system.

It includes:
- `populate_db.py` → creates and fills the database (run by owner(student) only)
- `professor_demo.py` → connects to the same database and runs example queries (professor)

Requirements

- Python 3.9 or newer
- Install dependencies:

pip install pymongo dnspython


Files Overview

'populate_db.py`
- Run by: Student only
- Purpose: Creates the MongoDB database, adds sample users, documents, and edits.
Note: small amount of users and documents added just for sake of implementation


 `queries_demo.py`
- Run by: Professor
- Purpose: Tests the database connection and verifies that read + write operations work.
- What it does:
  1. Lists all users.
  2. Lists all documents with collaborators.
  3. Lists all edits of *ProjectPlan*.
  4. Inserts a small test edit.

Run it with:

python queries_demo.py


Connection Information

If connecting manually through MongoDB Compass:

"
mongodb+srv://user:password@cluster0.pvzrzpb.mongodb.net/\

"

Database name:
online_document_editor_db

Note: Connections are already part of script.


