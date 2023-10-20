#!/usr/bin/env python3
"""
This module contains the function that returns all students
sorted by average score
"""
from pymongo import collection, command_cursor


def top_students(
        mongo_collection: collection.Collection
) -> command_cursor.CommandCursor:
    """
    Returns all students sorted by average score
    """
    students = mongo_collection.aggregate([{
        "$project": {
            "name": "$name",
            "averageScore": {
                "$avg": "$topics.score"
            }
        }
    }, {
        "$sort": {
            "averageScore": -1
        }
    }])
    return students
