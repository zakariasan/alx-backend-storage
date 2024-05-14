#!/usr/bin/env python3
""" Python function that lists all documents """


def update_topics(mongo_collection, name, topics):
    """ list all mongo_collections """
    data = mongo_collection.update_many({"name": name}, {"$set": {"topics":
                                                                  topics}})
    return data
