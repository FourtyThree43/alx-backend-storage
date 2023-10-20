#!/usr/bin/env python3
""" Module that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def main() -> None:
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    method_counts = {
        'GET': collection.count_documents({"method": "GET"}),
        'POST': collection.count_documents({"method": "POST"}),
        'PUT': collection.count_documents({"method": "PUT"}),
        'PATCH': collection.count_documents({"method": "PATCH"}),
        'DELETE': collection.count_documents({"method": "DELETE"})
    }

    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })

    # Get the top 10 most present IPs
    ip_counts = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")

    print("IPs:")
    for ip in ip_counts:
        print(f"\t{ip['_id']}: {ip['count']}")

    client.close()


if __name__ == "__main__":
    main()
