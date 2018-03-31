import data_layer


class BusinessLayer:
    """
    Perform business rules and directly interact with data layer
    """

    def __init__(self):
        self.dl = data_layer.DataLayer()
        self.documents_list = []

    def format_search_text(self, search_text):
        search_text = '\\b' + '.*\\b'.join(search_text.split()) + ".*"
        return search_text.strip()

    def get_names_by_default(self, search_text):
        search_text = self.format_search_text(search_text)
        cursor = self.dl.get_names_by_default(search_text)
        for document in cursor:
            # convert duration field to minutes and seconds
            self.documents_list.append(document)
        return self.documents_list

    def get_names_by_filter(self, search_text, field_filter):
        search_text = self.format_search_text(search_text)
        field_filter = field_filter.strip()

    def get_names_by_sort(self, search_text, sort_field):
        search_text = self.format_search_text(search_text)
        sort_field = sort_field.strip()

    def get_names_by_filter_sort(self, search_text, field_filter, sort_field):
        search_text = self.format_search_text(search_text)
        field_filter = field_filter.strip()
        sort_field = sort_field.strip()

    def add_comment(self, object_id, comment):
        comment = comment.strip()
        return self.dl.add_comment(object_id, comment)