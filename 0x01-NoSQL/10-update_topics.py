#!/usr/bin/env python3
"""This file contains the function for task 10.
"""


def update_topics(mongo_collection, name, topics):
    """This function updates all topics of a school document based on the name
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
