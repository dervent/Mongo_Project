import data_layer
import time


class BusinessLayer:
    """
    Perform business rules and directly interact with data layer.
    """

    def __init__(self):
        """
        Initialize data layer object and documents list.
        """
        self.dl = data_layer.DataLayer()
        self.documents_list = []

    def get_results(self, multiDict):
        """
        Performs search based on text and any filter and sort options.
        :param multiDict: MultiDict object that contains search text, and filter and sort options.
        :return: list of matching document titles.
        """
        search_text = self.format_search_text(multiDict['text'])
        if set(('filter', 'sort')) <= set(multiDict):
            field_filter = multiDict['filter'].strip().lower()
            sort_field = self.get_sort_field(multiDict['sort'].strip().lower())
            return self.get_names_by_filter_sort(search_text, field_filter, sort_field)
        elif 'filter' in multiDict:
            field_filter = multiDict['filter'].strip().lower()
            return self.get_names_by_filter(search_text, field_filter)
        elif 'sort' in multiDict:
            sort_field = self.get_sort_field(multiDict['sort'].strip().lower())
            return self.get_names_by_sort(search_text, sort_field)
        else:
            return self.get_names_by_default(search_text)

    def format_search_text(self, search_text):
        """
        Format the search string with RegEx patterns.
        :param search_text: user search text.
        :return: search text with RegEx patterns.
        """
        search_text = '\\b' + '.*\\b'.join(search_text.split()) + ".*"
        return search_text.strip()

    def get_sort_field(self, sort):
        """
        Use the user-selected sort option to return matching database field.
        :param sort: user-selected sort option.
        :return: matching database field.
        """
        if 'most viewed' in sort:
            return 'views'
        elif 'most recent' in sort:
            return 'film_date'
        elif 'most commented' in sort:
            return 'num_comments'

    def get_docs_in_list(self, cursor):
        """
        Populate a list object with each document found in Cursor object.
        :param cursor: Cursor object.
        :return: list object containing documents.
        """
        for document in cursor:
            self.documents_list.append(document)
        return self.documents_list

    def get_names_by_default(self, search_text):
        """
        Perform default search when no filter or sort option is specified.
        :param search_text: RegEx-formatted search text.
        :return: list object containing matching document titles/names.
        """
        cursor = self.dl.get_names_by_default(search_text)
        return self.get_docs_in_list(cursor)

    def get_names_by_filter(self, search_text, field_filter):
        """
        Perform search using only search text and filter option.
        :param search_text: RegEx-formatted search text.
        :param field_filter: field to filter by.
        :return: list object containing matching document titles/names.
        """
        cursor = self.dl.get_names_by_filter(search_text, field_filter)
        return self.get_docs_in_list(cursor)

    def get_names_by_sort(self, search_text, sort_field):
        """
        Perform search using only search text and sort option.
        :param search_text: RegEx-formatted search text.
        :param sort_field: field to sort by.
        :return: list object containing matching document titles/names.
        """
        cursor = self.dl.get_names_by_sort(search_text, sort_field)
        return self.get_docs_in_list(cursor)

    def get_names_by_filter_sort(self, search_text, field_filter, sort_field):
        """
        Perform search using search text, filter and sort option.
        :param search_text: RegEx-formatted search text.
        :param field_filter: field to filter by.
        :param sort_field: field to sort by.
        :return: list object containing matching document titles/names.
        """
        cursor = self.dl.get_names_by_filter_sort(search_text, field_filter, sort_field)
        return self.get_docs_in_list(cursor)

    def get_details(self, object_id):
        """
        Get details of single document.
        Format duration, film_date and views fields to present to users.
        Store name of image, if exists.
        :param object_id: ObjectId of the document.
        :return: dict object containing details of specified document.
        """
        document = self.dl.get_details(object_id)
        document['duration'] = time.strftime('%M:%S', time.gmtime(document['duration']))
        document['film_date'] = time.strftime('%m/%d/%Y', time.gmtime(document['film_date']))
        document['views'] = '{:,}'.format(document['views'])
        if 'image_id' in document:
            document['image_name'] = self.dl.get_image(document['image_id'])
        return document

    def add_comment(self, multiDict):
        """
        Add comment to single document, specified by ObjectId.
        :param multiDict: MultiDict object that contains the ObjectId and user comment.
        :return: 201 or 500 response code.
        """
        return self.dl.add_comment(multiDict['id'], multiDict['text'].strip())
