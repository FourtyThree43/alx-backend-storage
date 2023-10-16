#!/usr/bin/env python3
"""Module that changes all topics of a school document based on the name"""
from pymongo import collection
from typing import List


def update_topics(mongo_collection: collection.Collection, name: str,
                  topics: List[str]) -> None:
    """Changes all topics of a school document based on the name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
