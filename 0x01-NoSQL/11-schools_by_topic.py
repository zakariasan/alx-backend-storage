#!/usr/bin/env python3
""" Python function that lists all documents """


def schools_by_topic(mongo_collection, topic):
    """ list all mongo_collections """
    return mongo_collection.find({"topics": topic})
