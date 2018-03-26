import data_layer


class BusinessLayer:
    """
    Perform business rules and directly interact with data layer
    """

    def __init__(self):
        """
        Initialize attributes
        """
        self.dl = data_layer.DataLayer()
        self.documents_list = []

    def format_search_text(self, search_text):
        """
        Format the search string with RegEx patterns
        :param search_text: user-specified text
        :return: search string with RegEx patterns
        """
        search_text = '\\b' + '.*\\b'.join(search_text.split()) + ".*"
        return search_text.strip()

    def search_by_default(self, search_text):
        """
        Perform default search when no filter or sort is specified.
        :param search_text: user-specified text
        :return: list of matching documents
        """
        search_text = self.format_search_text(search_text)
        cursor = self.dl.search_by_default(search_text)
        for document in cursor:
            # convert duration field to minutes and seconds
            self.documents_list.append(document)
        return self.documents_list

    def search_by_filter(self, search_text, field_filter):
        """
        Perform search by filter option
        :param search_text: user-specified text
        :param field_filter: user-selected filter option
        :return: TBD
        """
        search_text = self.format_search_text(search_text)
        field_filter = field_filter.strip()

    def search_by_sort(self, search_text, sort_field):
        """
        Perform search by sort option
        :param search_text: user-specified text
        :param sort_field: user-selected sort option
        :return: TBD
        """
        search_text = self.format_search_text(search_text)
        sort_field = sort_field.strip()

    def search_by_filter_sort(self, search_text, field_filter, sort_field):
        """
        Perform search by filter and sort options
        :param search_text: user-specified text
        :param field_filter: user-selected filter option
        :param sort_field: user-selected sort option
        :return: TBD
        """
        search_text = self.format_search_text(search_text)
        field_filter = field_filter.strip()
        sort_field = sort_field.strip()

    def add_comment(self, object_id, comment):
        """
        Add comment to specific result (document)
        :param object_id: hidden object_id of document
        :param comment: user-specified comment strinf
        :return: Response object with status code of 201 (Created) or 500 (Internal Server Error)
        """
        comment = comment.strip()
        return self.dl.add_comment(object_id, comment)