from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb+srv://user:password@cluster0.pvzrzpb.mongodb.net/?retryWrites=true&w=majority")

db = client["online_document_editor_db"] # database

print("Connected successfully to MongoDB\n")


for user in db.users.find({}, {"_id": 0}):# example queries to see that db is working
    print(user)
print()


for doc in db.documents.find({}, {"_id": 0}):
    print(f"Document: {doc['name']}")
    for c in doc["collaborators"]:
        print(f"   Collaborator: {c['user_id']} → Role: {c['role']}")
    print()
print()


for edit in db.edits.find({"document_id": {"$exists": True}}, {"_id": 0}).sort("created_at", 1):
    print(edit)
print()

new_edit = {
    "document_id": db.documents.find_one({"name": "ProjectPlan"})["_id"],
    "user_id": db.users.find_one({"username": "bob"})["_id"],
    "username_cached": "bob",
    "body": "Professor test edit — added this line", # you can add any text here and add to edits
    "created_at": datetime.now()
}
result = db.edits.insert_one(new_edit)
print(f"Inserted new edit with ID: {result.inserted_id}")

print("\nScript completed successfully")
client.close()
