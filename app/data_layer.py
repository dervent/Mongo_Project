from pymongo import MongoClient
from pymongo import DESCENDING
from bson.objectid import ObjectId
import os
import flask
import gridfs


class DataLayer:
    """
    Query functions that directly interact with TedTalks database.
    """

    def __init__(self):
        """
        Initialize connection to MongoDB database instance hosted on mLab.
        Define fields to be excluded from queries.
        """
        self.client = MongoClient('ds237855.mlab.com', 37855)
        self.database = self.client["ted-talk-database"]
        self.database.authenticate("admin", "password")
        self.collection = self.database.Talks
        self.excluded_fields = {'ratings': 0, 'speaker_occupation': 0,
                                'related_talks':0, 'title': 0}

    def get_names_by_default(self, search_text):
        """
        Query Talks collection for documents that contain the Regex-formatted text in the name field.
        :param search_text: Regex-formatted text.
        :return: Cursor object containing matching documents.
        """
        return self.collection.find({'name': {'$regex': search_text, '$options': 'i'}}, {'name': 1})

    def get_names_by_filter(self, search_text, field_filter):
        """
        Query Talks collection for documents that contain the Regex-formatted text in the specified field.
        :param search_text: Regex-formatted text.
        :param field_filter: field in which to search for text.
        :return: Cursor object containing matching documents.
        """
        return self.collection.find({field_filter: {'$regex': search_text, '$options': 'i'}},
                                    self.excluded_fields)

    def get_names_by_sort(self, search_text, sort_field):
        """
        Query Talks collection for documents that contain the Regex-formatted text.
        Sort in descending order by the specified field.
        :param search_text: Regex-formatted text.
        :param sort_field: field used to sort documents.
        :return: Cursor object containing matching documents.
        """
        return self.collection.find({'name': {'$regex': search_text, '$options': 'i'}},
                                    self.excluded_fields).sort(sort_field, DESCENDING)

    def get_names_by_filter_sort(self, search_text, field_filter, sort_field):
        """
        Query Talks collection for documents that contain the Regex-formatted text in the specified field.
        Sort in descending order by the specified field.
        :param search_text: Regex-formatted text.
        :param field_filter: field in which to search for text.
        :param sort_field: field used to sort documents.
        :return: Cursor object containing matching documents.
        """
        return self.collection.find({field_filter: {'$regex': search_text, '$options': 'i'}},
                                    self.excluded_fields).sort(sort_field, DESCENDING)

    def get_details(self, object_id):
        """
        Query Talks collection for the details of the document, specified by the ObjectId
        :param object_id: ObjectId of the document.
        :return: dict object containing projected fields.
        """
        return self.collection.find_one({'_id': ObjectId(object_id)}, self.excluded_fields)

    def add_comment(self, object_id, comment):
        """
        Add comment to single document, specified by ObjectId.
        Update number of comments by 1.
        :param object_id: ObjectId of the document.
        :param comment: comment to add to the array of comments
        :return: 201 response indicating comment created in document, 500 response otherwise
        """
        update = self.collection.update_one({'_id': ObjectId(object_id)}, {'$push' : {'comments': comment},
                                                                           '$inc': {'num_comments': 1}})
        if update.matched_count == 1:
            return flask.Response(status=201)
        else:
            return flask.Response(status=500)

    def get_image(self, image_id):
        """
        Download document's corresponding image to localhost server.
        :param image_id: ObjectId() of image in GridFS.
        :return: name of image file.
        """
        fs = gridfs.GridFSBucket(self.database)
        doc = self.database.fs.files.find_one({'_id': ObjectId(image_id)})
        filename = doc['filename']
        if not os.path.exists(os.path.join(os.getcwd(), 'static\\media\\img\\' + filename)):
            file = open('static\\media\\img\\' + filename, 'wb')
            fs.download_to_stream(ObjectId(image_id), file)
            file.close()
        return filename