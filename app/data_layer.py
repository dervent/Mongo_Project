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
        """
        Initialize local connection to TedTalks database and Talks collection
        """
        self.client = MongoClient('localhost', 27017)
        self.database = self.client.TedTalks
        self.collection = self.database.Talks
        self.excluded_fields = {'main_speaker': 0, 'ratings': 0, 'speaker_occupation': 0, 'title': 0}

    def search_by_default(self, search_text):
        """
        When a filter (field) or sort is not specified, query for text in the default field, title
        :param search_text: user-specified text
        :return: cursor object containing all matching documents
        """
        return self.collection.find({'name': {'$regex': search_text, '$options': 'i'}},
                                    self.excluded_fields)

    def search_by_filter(self, search_text, field_filter):
        """
        Query for the text in the specified filter (field)
        :param search_text: user-specified text
        :param field_filter: user-selected field
        :return: cursor object containing all matching documents
        """
        return self.collection.find({field_filter: {'$regex': search_text, '$options': 'i'}},
                                    self.excluded_fields)

    def search_by_sort(self, search_text, sort_field):
        """
        Query for the text in the default field, title, then sort in ascending order
        by the sort option specified
        :param search_text: user-specified text
        :param sort_field: user-selected sort value
        :return: cursor object containing all matching documents
        """
        return self.collection.find({'name': {'$regex': search_text, '$options': 'i'}},
                                    self.excluded_fields).sort(sort_field, ASCENDING)

    def search_by_filter_sort(self, search_text, field_filter, sort_field):
        """
        Query for the for the text in the specified filter (field), then sort in ascending order
        by the sort option specified
        :param search_text: user-specified text
        :param field_filter: user-selected field
        :param sort_field: user-selected sort value
        :return: cursor object containing all matching documents
        """
        return self.collection.find({field_filter: {'$regex': search_text, '$options': 'i'}},
                                    self.excluded_fields).sort(sort_field, ASCENDING)

    def add_comment(self, object_id, comment):
        """
        Add the comment the user entered into the document specified by the BSON ObjectId
        :param object_id: BSON OBjectId()
        :param comment: user-specified textual comment
        :return: Response object with status code of 201 (Created) or 500 (Internal Server Error)
        """
        update = self.collection.update_one({'_id': ObjectId(object_id)}, {'$push' : {'comments': comment}})
        if update.matched_count == 1:
            return flask.Response(status=201)
        else:
            return flask.Response(status=500)

    def get_image(self, object_id):
        """
        TBD
        """
        self.collection = None