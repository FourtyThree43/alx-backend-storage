#!/usr/bin/env python3
"""
This module contains the function that returns all students
sorted by average score
"""
from pymongo.collection import Collection
from pymongo.command_cursor import CommandCursor


def top_students(mongo_collection: Collection) -> CommandCursor:
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
