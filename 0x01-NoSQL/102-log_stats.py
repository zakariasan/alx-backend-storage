#!/usr/bin/env python3
"""
Write a Python function that returns all students sorted by average score:
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """ try to log in """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    total = logs_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    counts = {method: logs_collection.count_documents(
        {"method": method}) for method in methods}
    path_count = logs_collection.count_documents({"method": "GET", "path":
                                                  "/status"})

    print(f"{total} logs")
    print("Methods:")
    for method, count in counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{path_count} status check")
