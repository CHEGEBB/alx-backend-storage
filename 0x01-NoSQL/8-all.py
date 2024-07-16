#!/usr/bin/env python3
"""This file contains the function for task 8.
"""


def list_all(mongo_collection):
    """
    It returns Lists all documents in a collection.
    """
    return list(mongo_collection.find({}))
