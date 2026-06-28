#!/usr/bin/env python3
"""MongoDB-də saxlanılan Nginx loqları barədə statistika verən skript"""
from pymongo import MongoClient


def log_stats():
    """Nginx loq kolleksiyasının statistikasını çap edir"""
    # MongoDB-yə qoşulma
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Verilənlər bazası və kolleksiyanı seçirik
    db = client.logs
    collection = db.nginx

    # 1. Ümumi sənəd (log) sayı
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Metodlar üzrə statistika
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 3. Xüsusi status yoxlanışı (method=GET, path=/status)
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
