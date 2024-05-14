#!/usr/bin/env python3
""" Python function that lists all documents """


def list_all(mongo_collection):
    """ list all mongo_collections """
    data = mongo_collection.find()
    res = []
    for d in data:
        res.append(d)
    return res
