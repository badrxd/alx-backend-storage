#!/usr/bin/env python3
"""function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """create a new document, and return the id """
    obj = mongo_collection.insert_one(kwargs)
    return obj.inserted_id
