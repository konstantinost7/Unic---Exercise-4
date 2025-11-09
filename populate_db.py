from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb+srv://db_user:Pass@cluster0.pvzrzpb.mongodb.net/?appName=Cluster0") # must add user and pass to run
db = client["online_document_editor_db"] #database



users = [
    {"username": "alice", "email": "alice@example.com", "name": "Alice", "lastname": "Doe", "created_at": datetime.now()},
    {"username": "bob", "email": "bob@example.com", "name": "Bob", "lastname": "Lee", "created_at": datetime.now()},
    {"username": "mark", "email": "mark@example.com", "name": "Mark", "lastname": "Smith", "created_at": datetime.now()}
]
user_ids = db.users.insert_many(users).inserted_ids

doc = {
    "name": "ProjectPlan",
    "owner_id": user_ids[0],
    "created_at": datetime.now(),
    "size": 0,
    "collaborators": [
        {"user_id": user_ids[0], "role": "owner",  "added_at": datetime.now()},
        {"user_id": user_ids[1], "role": "editor", "added_at": datetime.now()},
        {"user_id": user_ids[2], "role": "viewer", "added_at": datetime.now()}
    ]
}
doc_id = db.documents.insert_one(doc).inserted_id

edits = [
    {"document_id": doc_id, "user_id": user_ids[0], "username_cached": "alice",
     "body": "Created initial structure", "created_at": datetime.now()},
    {"document_id": doc_id, "user_id": user_ids[1], "username_cached": "bob",
     "body": "Added summary section", "created_at": datetime.now()},
    {"document_id": doc_id, "user_id": user_ids[2], "username_cached": "mark",
     "body": "Suggested formatting change", "created_at": datetime.now()}
]
db.edits.insert_many(edits)

print("Database populated successfully.")
client.close()
