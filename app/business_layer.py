import data_layer
import time


class BusinessLayer:
    """
    Perform business rules and directly interact with data layer
    """

    def __init__(self):
        self.dl = data_layer.DataLayer()
        self.documents_list = []

    def get_results(self, multiDict):
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
        search_text = '\\b' + '.*\\b'.join(search_text.split()) + ".*"
        return search_text.strip()

    def get_sort_field(self, sort):
        if 'most viewed' in sort:
            return 'views'
        elif 'most recent' in sort:
            return 'film_date'
        elif 'most commented' in sort:
            return 'num_comments'

    def get_docs_in_list(self, cursor):
        for document in cursor:
            self.documents_list.append(document)
        return self.documents_list

    def get_names_by_default(self, search_text):
        cursor = self.dl.get_names_by_default(search_text)
        return self.get_docs_in_list(cursor)

    def get_names_by_filter(self, search_text, field_filter):
        cursor = self.dl.get_names_by_filter(search_text, field_filter)
        return self.get_docs_in_list(cursor)

    def get_names_by_sort(self, search_text, sort_field):
        cursor = self.dl.get_names_by_sort(search_text, sort_field)
        return self.get_docs_in_list(cursor)

    def get_names_by_filter_sort(self, search_text, field_filter, sort_field):
        cursor = self.dl.get_names_by_filter_sort(search_text, field_filter, sort_field)
        return self.get_docs_in_list(cursor)

    def get_details(self, object_id):
        document = self.dl.get_details(object_id)
        document['duration'] = time.strftime('%M:%S', time.gmtime(document['duration']))
        document['film_date'] = time.strftime('%m/%d/%Y', time.gmtime(document['film_date']))
        document['views'] = '{:,}'.format(document['views'])
        return document

    def add_comment(self, multiDict):
        return self.dl.add_comment(multiDict['id'], multiDict['text'].strip())
