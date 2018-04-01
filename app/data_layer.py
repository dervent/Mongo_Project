from pymongo import MongoClient
from pymongo import ASCENDING
from bson.objectid import ObjectId
import flask
import gridfs


class DataLayer:
    """
    Query functions that directly interact with TedTalks database
    """

    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.database = self.client.TedTalks
        self.collection = self.database.Talks
        self.excluded_fields = {'main_speaker': 0, 'ratings': 0, 'speaker_occupation': 0,
                                'related_talks':0, 'title': 0}

    def get_names_by_default(self, search_text):
        return self.collection.find({'name': {'$regex': search_text, '$options': 'i'}}, {'name': 1})

    def get_names_by_filter(self, search_text, field_filter):
        return self.collection.find({field_filter: {'$regex': search_text, '$options': 'i'}},
                                    self.excluded_fields)

    def get_names_by_sort(self, search_text, sort_field):
        return self.collection.find({'name': {'$regex': search_text, '$options': 'i'}},
                                    self.excluded_fields).sort(sort_field, ASCENDING)

    def get_names_by_filter_sort(self, search_text, field_filter, sort_field):
        return self.collection.find({field_filter: {'$regex': search_text, '$options': 'i'}},
                                    self.excluded_fields).sort(sort_field, ASCENDING)

    def get_details(self, object_id):
        return self.collection.find_one({'_id': ObjectId(object_id)}, self.excluded_fields)

    def add_comment(self, object_id, comment):
        update = self.collection.update_one({'_id': ObjectId(object_id)}, {'$push' : {'comments': comment}})
        if update.matched_count == 1:
            return flask.Response(status=201)
        else:
            return flask.Response(status=500)
