#!/usr/bin/env python3
""" Python function that lists all documents """


def insert_school(mongo_collection, **kwargs):
    """ list all mongo_collections """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
