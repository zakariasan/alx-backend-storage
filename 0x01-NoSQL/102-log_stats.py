#!/usr/bin/env python3
"""
Write a Python function that returns all students sorted by average score:
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """ try to log in """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.server_logs.nginx_access_logs

    total_logs = logs_collection.count_documents({})
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: logs_collection.count_documents(
        {"method": method}) for method in http_methods}
    status_check_count = logs_collection.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"Total logs: {total_logs}")
    print("HTTP Methods:")
    for method, count in method_counts.items():
        print(f"\t{method}: {count}")
    print(f"Status check: {status_check_count}")

    print("Top 10 IPs:")
    top_ips = logs_collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    for i, ip_info in enumerate(top_ips, start=1):
        print(f"\t{i}. {ip_info['_id']}: {ip_info['count']}")
