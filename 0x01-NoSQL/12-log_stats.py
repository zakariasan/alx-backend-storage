#!/usr/bin/env python3
""" Python function that lists all documents """
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
collection = db.nginx

length = collection.count_documents({})

print(f"{length} logs")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

for met in methods:
    count = collection.count_documents({"method": met})
    print(f"    method {met}: {count}")

count_status = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{count_status} status check")
