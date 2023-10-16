#!/usr/bin/env python3
"""Module that returns the list of school having a specific topic"""
from pymongo import collection
from typing import List


def schools_by_topic(mongo_collection: collection.Collection,
                     topic: str) -> List:
    """Method that returns the list of school having a specific topic"""
    return list(mongo_collection.find({"topics": topic}))
