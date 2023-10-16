#!/usr/bin/env python3
""" Module that inserts a new document in a collection based on kwargs"""
from pymongo import collection
from typing import Any


def insert_school(mongo_collection: collection.Collection, **kwargs) -> Any:
    """ Method that inserts a new document in a collection based on kwargs"""
    new_doc = mongo_collection.insert_one(kwargs)

    return new_doc.inserted_id
