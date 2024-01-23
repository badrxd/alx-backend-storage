#!/usr/bin/env python3
"""lists all documents in a collection"""


def list_all(mongo_collection):
    """lists all documents in a collection mongo_collection"""
    if mongo_collection is None:
        return []
    return [x for x in mongo_collection.find()]
