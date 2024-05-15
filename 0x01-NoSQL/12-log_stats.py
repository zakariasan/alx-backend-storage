#!/usr/bin/env python3
""" Python function that lists all documents """
from pymongo import MongoClient


if __name__ == "__main__":
    """ try to log stats"""
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the logs collection
    logs_collection = client.logs.nginx
    # Count total number of logs
    total_logs = logs_collection.count_documents({})
    # Count number of logs for each HTTP method
    get_logs = logs_collection.count_documents({"method": "GET"})
    post_logs = logs_collection.count_documents({"method": "POST"})
    put_logs = logs_collection.count_documents({"method": "PUT"})
    patch_logs = logs_collection.count_documents({"method": "PATCH"})
    delete_logs = logs_collection.count_documents({"method": "DELETE"})
    # Count number of logs with method=GET and path=/status
    status_check_logs = logs_collection.count_documents({"method": "GET",
                                                         "path": "/status"})
    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_logs}")
    print(f"\tmethod POST: {post_logs}")
    print(f"\tmethod PUT: {put_logs}")
    print(f"\tmethod PATCH: {patch_logs}")
    print(f"\tmethod DELETE: {delete_logs}")
    print(f"{status_check_logs} status check")
